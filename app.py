import streamlit as st
from utils.data_loader import load_data, merge_data
from utils.risk_engine import compute_risk_score
from utils.allocation import allocate_ward
from utils.simulation import simulate_vitals
from utils.visualization import bed_heatmap, resource_graph, patient_timeline
from models.risk_model import train_model, predict_risk

st.set_page_config(page_title="Hospital Digital Twin", layout="wide")

st.title("🏥 Hospital Digital Twin - ICU Command Center")

# Load data
patients, telemetry, prescriptions = load_data()
df = merge_data(patients, telemetry, prescriptions)
train_model(df)
df = predict_risk(df)

# Sidebar controls
st.sidebar.header("Simulation Controls")

simulate = st.sidebar.button("Run Simulation")
icu_capacity = st.sidebar.slider("ICU Beds", 5, 50, 10)
general_capacity = st.sidebar.slider("General Beds", 10, 100, 20)

# Process pipeline
df = compute_risk_score(df)

if simulate:
    df = simulate_vitals(df)
    df = compute_risk_score(df)

df = allocate_ward(df, icu_capacity, general_capacity)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("ICU Bed Heatmap")
    st.plotly_chart(bed_heatmap(df), use_container_width=True)

with col2:
    st.subheader("Resource Consumption")
    st.plotly_chart(resource_graph(df), use_container_width=True)

st.subheader("Patient Flow Timeline")
st.plotly_chart(patient_timeline(df), use_container_width=True)

# Table view
st.subheader("Live Patient Table")
st.dataframe(df)