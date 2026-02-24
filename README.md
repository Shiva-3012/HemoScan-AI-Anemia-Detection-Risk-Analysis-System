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

 Project Structure 
Step 1: Main Application File

app.py
This is the Streamlit web application file.
It handles:

User input

Risk prediction

Safety recommendations

Graph visualization

Clinical receipt generation

Step 2: Model Training Script

model_training.py
This file:

Loads the dataset

Performs preprocessing

Applies feature scaling

Trains the Logistic Regression model

Saves the trained model (model.pkl)

Saves the scaler (scaler.pkl)

Step 3: Model Directory

model/ folder
This folder stores:

model.pkl → Trained machine learning model

scaler.pkl → StandardScaler used during training

These files are required for prediction inside the web app.

Step 4: Dataset Directory

data/ folder
Contains:

anemia_dataset.csv → Original dataset

cleaned_anemia_dataset.csv → Preprocessed dataset used for training

Step 5: Requirements File

requirements.txt
Contains all required Python libraries:

Streamlit

Pandas

NumPy

Scikit-learn

Matplotlib

Used to install dependencies before running the project.

Step 6: Documentation

README.md
Contains:

Project overview

Setup instructions

Features

Business impact

Author information
