# 🏗️ InfraRisk AI – Infrastructure Finance Risk Modelling

InfraRisk AI is an AI-powered system that integrates infrastructure project analytics, macroeconomic indicators, and financial risk modelling to assess credit risk and estimate potential financial losses in infrastructure finance.

---

## 🚀 Overview

This project simulates a real-world infrastructure finance platform where risk is influenced by:

* 🏗️ Project delays (construction & execution risk)
* 🌍 Macroeconomic conditions (GDP growth, inflation, interest rates)
* 💰 Financial exposure (project cost & credit risk)

The system predicts the overall risk of infrastructure projects and provides financial loss estimation for better decision-making.

---

## 🔥 Key Features

* 📊 Infrastructure Project Risk Prediction
* 🌍 Macroeconomic Risk Integration
* 💳 Credit Risk Consideration
* 💰 Financial Loss Estimation
* 📈 Interactive Streamlit Dashboard

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 🧠 How It Works

1. Data is derived from supply chain dataset (used as proxy for infrastructure data)
2. Feature engineering creates:

   * Project Cost
   * Delay
   * Macroeconomic variables
3. Machine Learning model (Random Forest) predicts infrastructure risk
4. Risk probability is used to calculate expected financial loss

---

## 📊 Model Inputs

* Project Cost
* Delay (days)
* Interest Rate (%)
* GDP Growth (%)
* Inflation (%)

---

## 📈 Outputs

* Risk Probability
* Risk Level (Low / Medium / High)
* Estimated Financial Loss

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 📸 Demo

(Add your dashboard screenshot here)

---

## 🎯 Use Case

* Infrastructure Finance
* Credit Risk Assessment
* Project Investment Analysis
* Development Finance Institutions (DFIs)

---

## 👨‍💻 Author

Subhash Patel

---

## 💡 Future Improvements

* Integration with real macroeconomic datasets
* Advanced geospatial risk modelling
* Portfolio-level risk simulation
* Real-time data pipelines

---
