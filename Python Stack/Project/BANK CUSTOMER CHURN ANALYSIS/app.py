import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load model and scaler
@st.cache_resource
def load_model():
    with open("optimized_xgb_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

@st.cache_resource
def load_scaler():
    return joblib.load("scaler.pkl")  # Ensure it matches the 9 features


# Streamlit UI
st.title("🚀 Bank Customer Churn Prediction Dashboard")

# Load model & scaler
model = load_model()
scaler = load_scaler()

# Define actual feature names
feature_names = ['credit_score', 'age', 'tenure', 'balance', 'products_number',
       'credit_card', 'active_member']

# Extract feature importance
feature_importance = model.feature_importances_

# Ensure correct length
if len(feature_importance) != len(feature_names):
    st.error("❌ Feature importance mismatch! Check feature list.")
else:
    # Create a DataFrame for plotting
    feature_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": feature_importance
    }).sort_values(by="Importance", ascending=False)

    # Feature Importance Visualization
    st.write("### 🔥 Feature Importance")
    fig, ax = plt.subplots()
    sns.barplot(x="Importance", y="Feature", data=feature_df, ax=ax)
    ax.set_xlabel("Importance Score")
    ax.set_ylabel("Features")
    st.pyplot(fig)

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload a CSV file for batch prediction", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### 📊 Data Preview")
    st.write(df.head())

# Function to preprocess user input
def preprocess_input(user_input, scaler):
    user_input_array = np.array(user_input).reshape(1, -1)
    return scaler.transform(user_input_array)



def predict_churn(model, user_input, scaler):
    # Ensure input is correctly preprocessed
    processed_input = scaler.transform(np.array(user_input).reshape(1, -1))  

    # Predict probabilities
    prob_no_churn, prob_churn = model.predict_proba(processed_input)[0]  # [0] -> No Churn, [1] -> Churn
    
    return prob_churn  # Return churn probability



# Predict Churn for a Single Customer
st.write("### 🤖 Predict Churn for a New Customer")

# Collect user input
credit_score = st.number_input("📉 Credit Score", 300, 850, 650)
gender = st.selectbox("🧑 Gender", [0, 1])  # 0 for Female, 1 for Male
age = st.number_input("🎂 Age", 18, 100, 35)
tenure = st.number_input("📆 Tenure (Years)", 0, 10, 5)
balance = st.number_input("💰 Balance", 0.0, 250000.0, 50000.0)
products_number = st.selectbox("📦 Number of Products", [1, 2, 3, 4])
credit_card = st.selectbox("💳 Has Credit Card?", [0, 1])  # 0: No, 1: Yes
active_member = st.selectbox("🟢 Active Member?", [0, 1])  # 0: No, 1: Yes
estimated_salary = st.number_input("💵 Estimated Salary", 0.0, 200000.0, 50000.0)
user_input = [credit_score, age, tenure, balance, products_number, credit_card, active_member]

THRESHOLD = 0.6

if st.button("🔍 Predict Churn"):
    probability = predict_churn(model, user_input, scaler)
    st.write(f"### 🔮 Churn Probability: {probability:.2f}")

    if probability > THRESHOLD:
        st.error("⚠️ High Risk of Churn! Consider retention strategies.")
    else:
        st.success("✅ Low Risk of Churn")  
