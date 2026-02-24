#  HemoScan AI  
### Anemia Detection & Risk Analysis System  

HemoScan AI is a Machine Learning-powered Clinical Decision Support System designed to predict anemia using Complete Blood Count (CBC) parameters.  

The system analyzes hemoglobin levels and red blood cell indices to provide early risk detection, probability scoring, and patient safety recommendations.

---

##  Project Overview

Anemia is a widespread global health issue affecting millions of people. Early detection is essential to prevent complications.

HemoScan AI provides:
- ✔ Binary Anemia Classification (Detected / Not Detected)
- ✔ Risk Probability Score (%)
- ✔ Risk Stratification (Safe / Medium / High / Critical)
- ✔ Patient Safety & Preventive Measures
- ✔ Standardized Feature Impact Visualization
- ✔ Downloadable Clinical Report

This project demonstrates the application of Machine Learning in healthcare for preventive screening and decision support.

---

##  Problem Statement

Manual screening of anemia can be time-consuming and dependent on clinical interpretation.  
There is a need for an automated, scalable, and affordable screening tool that assists healthcare professionals in early anemia detection.

---

## Proposed Solution

We developed a machine learning model trained on CBC parameters to:

- Predict anemia presence
- Calculate probability of risk
- Categorize patients into risk levels
- Provide preventive recommendations
- Support clinical decision-making

The system is deployed as a Streamlit web application for easy accessibility.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- StandardScaler
- Streamlit
- Matplotlib

---

##  Input Parameters

The system uses the following CBC parameters:

- Gender
- Hemoglobin (g/dL)
- MCH (Mean Corpuscular Hemoglobin)
- MCHC (Mean Corpuscular Hemoglobin Concentration)
- MCV (Mean Corpuscular Volume)

---

##  Model Workflow

1. Data Cleaning & Preprocessing  
2. Feature Scaling using StandardScaler  
3. Model Training using Logistic Regression  
4. Model Evaluation  
5. Saving Model & Scaler  
6. Deployment via Streamlit  

---

##  Risk Classification Logic

| Probability | Risk Level |
|-------------|------------|
| < 30% | SAFE |
| 30–60% | MEDIUM RISK |
| 60–85% | HIGH RISK |
| > 85% | CRITICAL RISK |

---

##  Project Structure
HemoScan-AI/
│── app.py
│── model_training.py
│── requirements.txt
│── README.md
│
├── model/
│ ├── model.pkl
│ ├── scaler.pkl
│
├── data/
│ ├── anemia_dataset.csv
│ ├── cleaned_anemia_dataset.csv
