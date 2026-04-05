# 🏥 Hospital Digital Twin – ICU Command Center

A real-time Hospital Digital Twin System built using Streamlit, Machine Learning, and Data Engineering principles to simulate, predict, and optimize ICU operations under critical conditions.

# 🚀 Project Overview

This project models a virtual ICU environment where:

Patient vitals continuously update

Risk scores are dynamically computed

Beds are allocated automatically

Resource usage is predicted

ICU operations are visualized in real-time

It solves the challenge of managing a highly volatile healthcare ecosystem with limited resources.


# 🎯 Key Features

# 🧠 Intelligent Risk Prediction

Machine Learning-based risk scoring using patient vitals

Handles missing values using preprocessing pipelines

Predicts critical patients in real-time

# 🏨 Automated Ward Allocation

ICU vs General ward assignment

Based on:

Risk score

Bed availability

Priority-based routing system

# 📊 Interactive Dashboard (Streamlit)

# 🔴 ICU Bed Heatmap

Visual representation of patient distribution

Risk intensity shown using color gradients

📈 Resource Consumption Graph

Tracks ICU load trends over time

Helps predict system stress

🧍 Patient Flow Timeline

Tracks patient movement and risk progression

🎛️ Simulation Control Panel

Adjust ICU capacity

Run real-time simulation

Observe dynamic changes

🔄 Real-Time Simulation Engine

Simulates changing vitals (heart rate, SpO2)

Mimics real ICU conditions

Enables stress testing of the system

# 🗂️ Project Structure

hospital_digital_twin/
│
├── app.py                      
├── data/
│   ├── patient_demographics.csv
│   ├── telemetry_logs.csv
│   └── prescriptions.csv
│
├── utils/
│   ├── data_loader.py
│   ├── risk_engine.py
│   ├── allocation.py
│   ├── simulation.py
│   └── visualization.py
│
├── models/
│   ├── risk_model.py
│   ├── risk_model.pkl
│   └── scaler.pkl
│
├── config/
│   └── settings.py
│
└── requirements.txt


# ⚙️ Installation & Setup

# 1️⃣ Clone the Repository

git clone https://github.com/your-username/hospital-digital-twin.git

cd hospital-digital-twin

# 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv

Activate:

Windows

venv\Scripts\activate
Mac/Linux
Bash
source venv/bin/activate
3️⃣ Install Dependencies
Bash
pip install -r requirements.txt
4️⃣ Run the Application

streamlit run app.py

Open in browser:

http://localhost:8501

# 📊 Dataset Information

The system uses three datasets:

File

Description

patient_demographics.csv

Patient info (age, ID, etc.)

telemetry_logs.csv

Real-time vitals (heart rate, SpO2)

prescriptions.csv

Medication data

# 🧠 Machine Learning Model
Model: Logistic Regression

Features:

Heart Rate (from hex)

SpO2

Age

Output:

Risk Score (0–1 probability)

# 🔧 Data Handling

Missing values handled using median imputation

Feature scaling applied using StandardScaler

Pipeline-based preprocessing ensures robustness

⚠️ Common Issues & Fixes

❌ NaN Error in Model

✔ Fixed using:

Python

SimpleImputer(strategy="median")

❌ File Not Found

✔ Ensure:

data/*.csv files exist

❌ Wrong Column Names

✔ Required columns:

internal_id

heart_rate_hex

spO2

age
# 🔥 Advanced Features (Future Scope)

✅ XGBoost / Deep Learning model

✅ Real-time streaming using Kafka

✅ ICU alert system 🚨

✅ Duplicate patient detection (ghost ID logic)

✅ Role-based dashboard (Admin/Doctor)

✅ Cloud deployment (AWS / Render)


# 💡 Use Cases

ICU capacity planning

Emergency response simulation

Hospital resource optimization

Predictive healthcare analytics

# 🏆 Why This Project Stands Out

✔ Combines ML + Data Engineering + Visualization

✔ Real-world healthcare simulation

✔ Scalable and modular architecture

✔ Handles real-world data issues (missing values)

✔ Interactive and decision-focused dashboard

# 👩‍💻 Author

Sangita Bera

Aspiring Data Scientist | Backend Developer | Digital Creator

# ⭐ Support

If you like this project:

⭐ Star the repo

🍴 Fork it

📢 Share it

# 🚀 Final Note

This project is not just a dashboard —
it’s a mini hospital intelligence system designed to simulate real-world ICU decision-making.
