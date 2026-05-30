import streamlit as st
import pandas as pd
import pickle
import os

os.environ["LOKY_MAX_CPU_COUNT"] = "1"

st.set_page_config(page_title="InfraRisk AI", layout="centered")

st.title("🏗️ InfraRisk AI")
st.caption("Infrastructure Finance Risk Prediction System")

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return pickle.load(open("model_ir.pkl", "rb"))

model = load_model()

# ---------------- INPUTS ----------------
st.subheader("📥 Enter Project Details")

project_cost = st.number_input("Project Cost (₹)", value=1000000)
delay = st.slider("Project Delay (days)", 0, 20, 5)
interest_rate = st.slider("Interest Rate (%)", 1, 20, 8)
gdp_growth = st.slider("GDP Growth (%)", 1, 10, 6)
inflation = st.slider("Inflation (%)", 1, 10, 5)

# ---------------- PREDICTION ----------------
input_df = pd.DataFrame([{
    'project_cost': project_cost,
    'delay': delay,
    'interest_rate': interest_rate,
    'gdp_growth': gdp_growth,
    'inflation': inflation
}])

prob = model.predict_proba(input_df)[0][1]

# ---------------- RISK LEVEL ----------------
if prob < 0.3:
    level = "Low 🟢"
elif prob < 0.7:
    level = "Medium 🟡"
else:
    level = "High 🔴"

# ---------------- LOSS ----------------
loss = prob * project_cost

# ---------------- OUTPUT ----------------
st.subheader("📊 Results")

st.metric("Risk Probability", f"{prob*100:.2f}%")
st.metric("Risk Level", level)
st.metric("Estimated Loss (₹)", f"{loss:,.0f}")

st.progress(int(prob * 100))

st.markdown("---")
st.caption("Developed by Subhash Patel 🚀")