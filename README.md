# 🏥 Hospital Digital Twin – ICU Command Center

> A real-time Hospital Digital Twin System designed to simulate, monitor, predict, and optimize ICU operations under critical healthcare conditions using Machine Learning, Streamlit, and Data Engineering concepts.


# 📌 Project Overview

The **Hospital Digital Twin** is a virtual representation of an ICU environment that continuously processes patient telemetry, demographics, and prescription data to:

- Predict patient risk levels
- Allocate ICU beds dynamically
- Simulate real-time hospital conditions
- Monitor resource consumption
- Improve operational decision-making

This system is designed to handle a highly volatile healthcare ecosystem where patient admissions, changing vitals, and resource limitations must be managed intelligently.


# 🚀 Features

## 🧠 Intelligent Risk Prediction
- Machine Learning-based patient risk scoring
- Predicts critical conditions using:
  - Heart Rate
  - SpO2
  - Age
- Logistic Regression-based predictive model
- Handles missing values using preprocessing pipelines


## 🏨 Automated Ward Allocation
Automatically assigns patients to:
- ICU Ward
- General Ward
- Waiting Queue

Based on:
- Risk score
- Bed capacity
- Patient priority


## 📊 Operational Command Dashboard

### 🔴 ICU Bed Heatmap
Visualizes:
- Bed occupancy
- Risk concentration
- ICU distribution


### 📈 Resource Consumption Graph
Tracks:
- ICU load
- Risk trends
- Operational pressure


### 🧍 Patient Flow Timeline
Displays:
- Patient movement
- Risk evolution
- Ward transitions


### 🎛️ Simulation Control Panel
Interactive controls for:
- ICU capacity
- General ward capacity
- Running real-time simulations


## 🔄 Real-Time Simulation Engine
Simulates:
- Dynamic heart rate changes
- Oxygen fluctuation
- ICU stress conditions


# 🧱 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| Streamlit | Dashboard UI |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Plotly | Interactive Visualizations |
| Scikit-Learn | Machine Learning |
| Joblib | Model Serialization |


## 📊 Dataset Information
The project uses three datasets:
- patient_demographics.csv
- telemetry_logs.csv
- prescriptions.csv

## 🧠 Machine Learning Pipeline
**Model Used**
- Logistic Regression
  
**Features Used**
- Heart Rate
- SpO2
- Age
- 
## ML Workflow

Raw Data
   ↓
Data Cleaning
   ↓
Missing Value Handling
   ↓
Feature Engineering
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Risk Prediction
   ↓
Ward Allocation


## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/hospital-digital-twin.git
cd hospital-digital-twin
```

### 2️⃣ Create Virtual Environment
Windows
```bash
python -m venv venv
venv\Scripts\activate
```
Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Running the Project
```bash
streamlit run app.py
```

## 🌐 Streamlit Dashboard
**After running:**
http://localhost:8501
Open this URL in your browser.

## 📦 Requirements
- streamlit
- pandas
- numpy
- plotly
- scikit-learn
- joblib


### 🧪 Model Training
The system automatically:
- Loads patient data
- Preprocesses features
- Handles missing values
- Trains Logistic Regression model
- Predicts risk scores
  
### 🔥 Risk Score Logic
- Patients are classified as high risk based on:
- High heart rate
- Low oxygen level
- Advanced age

### 🛠️ Missing Value Handling
- Healthcare data often contains missing values.
**This project uses:**
- Python
- SimpleImputer(strategy="median") to ensure robust predictions.

### 📈 Dashboard Components
ICU Heatmap
**Shows:**
- Bed utilization
- Patient risk intensity
- Resource Trend Graph

**Tracks:**
- Risk score progression
- ICU pressure over time
- Patient Timeline

**Displays:**
- Patient movement
- Operational flow


## 🔐 Production-Level Features
Potential enterprise upgrades:

- API Rate Limiting
- Logging & Monitoring
- CI/CD Pipeline
- MySQL/PostgreSQL Integration
- FastAPI Backend
- Real-time Telemetry Streaming

## 💡 Use Cases
- ICU Monitoring
- Resource Optimization
- Hospital Operations
- Emergency Simulation
- Healthcare Analytics
  
## 🏆 Key Highlights
✔ Real-time ICU Simulation
✔ Automated Bed Allocation
✔ Machine Learning Risk Prediction
✔ Interactive Dashboard
✔ Modular Architecture
✔ Scalable Design
✔ Production-Oriented Structure


### 👩‍💻 Author
Sangita Bera | Data Science Enthusiast | Backend Developer | ML & AI Learner

### ⭐ GitHub Support
If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

