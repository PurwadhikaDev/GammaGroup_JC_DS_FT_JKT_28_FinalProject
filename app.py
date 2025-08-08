import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Paste the same function here! ---
def feature_engineering(df):
    df = df.copy()
    df['AvgMonthlyCost'] = df['TotalCharges'] / df['tenure'].replace(0, np.nan)
    df['TenureGroup'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 36, 72],
        labels=['ShortTerm', 'MidTerm', 'LongTerm'],
        right=False
    )
    service_cols = [
        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    df['TotalServices'] = df[service_cols].apply(lambda x: np.sum(x == 'Yes'), axis=1)
    df['HasStreaming'] = ((df['StreamingTV'] == 'Yes') | (df['StreamingMovies'] == 'Yes')).astype(int)
    df['IsHighSpender'] = (df['MonthlyCharges'] > df['MonthlyCharges'].median()).astype(int)
    df['PaperlessAndElectronic'] = (
        (df['PaperlessBilling'] == 'Yes') & (df['PaymentMethod'].str.contains('electronic', case=False))
    ).astype(int)
    df['HasPartnerOrDependents'] = (
        (df['Partner'] == 'Yes') | (df['Dependents'] == 'Yes')
    ).astype(int)
    df['IsNewCustomer'] = (df['tenure'] < 6).astype(int)
    return df

@st.cache_resource
def load_pipeline():
    return joblib.load('best_catboost_pipeline.pkl')
pipeline = load_pipeline()

# Define the columns you expect
input_fields = {
    'gender': ['Male', 'Female'],
    'SeniorCitizen': ['Yes', 'No'],
    'Partner': ['Yes', 'No'],
    'Dependents': ['Yes', 'No'],
    'tenure': (0, 72),
    'PhoneService': ['Yes', 'No'],
    'MultipleLines': ['No phone service', 'No', 'Yes'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No internet service', 'No', 'Yes'],
    'OnlineBackup': ['No internet service', 'No', 'Yes'],
    'DeviceProtection': ['No internet service', 'No', 'Yes'],
    'TechSupport': ['No internet service', 'No', 'Yes'],
    'StreamingTV': ['No internet service', 'No', 'Yes'],
    'StreamingMovies': ['No internet service', 'No', 'Yes'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['Yes', 'No'],
    'PaymentMethod': [
        'Electronic check', 'Mailed check', 
        'Bank transfer (automatic)', 'Credit card (automatic)'
    ],
    'MonthlyCharges': (0.0, 200.0),
    'TotalCharges': (0.0, 10000.0)
}

st.title("Customer Churn Prediction")

st.write("Fill the form below to predict customer churn:")

# Create a form for user input
with st.form("churn_form"):
    input_data = {}
    for field, opts in input_fields.items():
        if isinstance(opts, list):
            input_data[field] = st.selectbox(field, opts)
        else:  # tuple is for numeric
            minv, maxv = opts
            if 'int' in str(type(minv)):
                input_data[field] = st.slider(field, int(minv), int(maxv), int(minv))
            else:
                input_data[field] = st.slider(field, float(minv), float(maxv), float(minv))
    submit = st.form_submit_button("Predict")

if submit:
    # Make a DataFrame from single input
    user_df = pd.DataFrame([input_data])
    # Predict using pipeline
    pred = pipeline.predict(user_df)[0]
    prob = pipeline.predict_proba(user_df)[0, 1]
    label = "Churn" if pred == 1 else "Not Churn"
    st.success(f"Prediction: **{label}**")
    st.info(f"Churn Probability: **{prob:.2%}**")
