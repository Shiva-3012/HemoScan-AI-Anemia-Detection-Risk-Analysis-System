import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Clinical Anemia Risk Assessment",
    page_icon="🩸",
    layout="centered"
)

# ---------------- LOAD MODEL + SCALER ----------------
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

if "page" not in st.session_state:
    st.session_state.page = "input"

# ---------------- MEDICAL BLUE THEME ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e3f2fd, #ffffff);
}
.title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0d47a1;
}
.subtitle {
    text-align:center;
    font-size:16px;
    color:#1565c0;
    margin-bottom:25px;
}
h3 {
    color:#0d47a1 !important;
    font-weight:bold !important;
}
label {
    color:#0d47a1 !important;
    font-weight:600 !important;
}
.result-box {
    background:white;
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-weight:bold;
    color:#0d47a1;
    border-left:6px solid #1565c0;
}
button[kind="primary"] {
    background: linear-gradient(90deg,#1565c0,#0d47a1);
    color:white;
    border-radius:8px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🩸 Clinical Decision Support System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Early Anemia Risk Assessment</div>', unsafe_allow_html=True)

# ================= INPUT PAGE =================
if st.session_state.page == "input":

    st.subheader("Enter Patient Clinical Parameters")

    gender = st.selectbox("Gender", ["Select", "Male", "Female"])

    hemoglobin = st.text_input("Hemoglobin (g/dL)")
    mch = st.text_input("MCH (pg)")
    mchc = st.text_input("MCHC (g/dL)")
    mcv = st.text_input("MCV (fL)")

    if st.button("Run Clinical Risk Assessment", type="primary"):

        if gender == "Select":
            st.error("Please select Gender.")
            st.stop()

        if not hemoglobin or not mch or not mchc or not mcv:
            st.error("All fields must be filled.")
            st.stop()

        try:
            hemoglobin = float(hemoglobin)
            mch = float(mch)
            mchc = float(mchc)
            mcv = float(mcv)
        except:
            st.error("Please enter valid numeric values.")
            st.stop()

        if hemoglobin <= 0 or mch <= 0 or mchc <= 0 or mcv <= 0:
            st.error("Values must be positive.")
            st.stop()

        gender_val = 0 if gender == "Male" else 1
        raw_input = np.array([[gender_val, hemoglobin, mch, mchc, mcv]])
        scaled_input = scaler.transform(raw_input)

        st.session_state.scaled_input = scaled_input
        st.session_state.raw_input = raw_input
        st.session_state.gender = gender
        st.session_state.hemoglobin = hemoglobin
        st.session_state.mch = mch
        st.session_state.mchc = mchc
        st.session_state.mcv = mcv
        st.session_state.page = "result"
        st.rerun()

# ================= RESULT PAGE =================
elif st.session_state.page == "result":

    scaled_input = st.session_state.scaled_input
    raw_input = st.session_state.raw_input

    prediction = model.predict(scaled_input)[0]
    prob = model.predict_proba(scaled_input)[0][1]

    risk_percentage = prob * 100
    status = "Anemia Detected" if prediction == 1 else "No Anemia Detected"

    if risk_percentage < 30:
        risk_level = "SAFE"
    elif risk_percentage < 60:
        risk_level = "MEDIUM RISK"
    elif risk_percentage < 85:
        risk_level = "HIGH RISK"
    else:
        risk_level = "CRITICAL RISK"

    st.markdown(
        f"""
        <div class="result-box">
        Diagnosis: {status}<br>
        Risk Level: {risk_level}<br>
        Probability: {risk_percentage:.2f}%
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- SAFETY MEASURES ----------------
    st.subheader("Patient Safety & Preventive Measures")

    if risk_percentage < 30:
        st.success("""
        ✔ Blood values are within normal range.
        ✔ Maintain balanced iron-rich diet.
        ✔ Routine annual CBC check-up recommended.
        ✔ Stay hydrated and maintain healthy lifestyle.
        """)

    elif risk_percentage < 60:
        st.warning("""
        ⚠ Mild deviation detected.
        ⚠ Increase iron & Vitamin B12 intake.
        ⚠ Repeat CBC test within 3–6 months.
        ⚠ Monitor symptoms like fatigue or weakness.
        """)

    elif risk_percentage < 85:
        st.error("""
        🚨 Significant anemia indicators detected.
        🚨 Immediate clinical consultation recommended.
        🚨 Doctor may prescribe iron supplementation.
        🚨 Avoid heavy physical exertion until evaluated.
        """)

    else:
        st.error("""
        🚨 CRITICAL RISK LEVEL.
        🚨 Seek urgent medical attention immediately.
        🚨 Advanced diagnostic testing required.
        🚨 Risk of complications if untreated.
        """)

    # ---------------- GRAPH ----------------
    st.subheader("Standardized Parameter Impact")

    features = ["Gender", "Hemoglobin", "MCH", "MCHC", "MCV"]
    impact_values = np.abs(scaled_input[0])

    fig, ax = plt.subplots()
    ax.bar(features, impact_values)
    ax.set_ylabel("Standardized Magnitude")
    ax.set_title("Feature Contribution (Scaled Input)")
    plt.xticks(rotation=20)
    st.pyplot(fig)

    # ---------------- RECEIPT DOWNLOAD ----------------
    receipt = f"""
==========================================
           ANEMIA CLINICAL REPORT
==========================================

Patient Details
------------------------------------------
Gender        : {st.session_state.gender}

Clinical Parameters
------------------------------------------
Hemoglobin    : {st.session_state.hemoglobin} g/dL
MCH           : {st.session_state.mch} pg
MCHC          : {st.session_state.mchc} g/dL
MCV           : {st.session_state.mcv} fL

------------------------------------------
Diagnosis     : {status}
Risk Level    : {risk_level}
Probability   : {risk_percentage:.2f}%

------------------------------------------
AI Clinical Decision Support System
Healthcare Hackathon Project
==========================================
"""

    st.download_button(
        "📄 Download Anemia Clinical Receipt",
        receipt,
        file_name="Anemia_Clinical_Report.txt"
    )

    if st.button("⬅ New Patient"):
        st.session_state.page = "input"
        st.rerun()