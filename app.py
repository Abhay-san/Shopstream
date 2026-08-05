import streamlit as st
import pandas as pd
import joblib

# Load Model and Scaler
model = joblib.load("high_value_order_xgb_pipeline_final (1).pkl")
scaler = joblib.load("scaler.pkl")

# ----------------------------
# Page Title
# ----------------------------

st.set_page_config(page_title="E-Commerce Order Prediction", page_icon="🛒")

st.title("🛒 E-Commerce High Value Order Prediction")

st.write("Predict whether an order is a High Value Order.")

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.markdown("""
### 📌 Project Information

**Project:** E-Commerce High Value Order Prediction

**Model:** XGBoost Classifier

**Dataset:** E-Commerce Orders Dataset

**Task:** Classification

**Framework:** Streamlit

**Developed by:** Abhay Mahajan
""")
# ----------------------------
# User Inputs
# ----------------------------

year = st.number_input("Year", 2023, 2030, 2023)

month = st.number_input("Month",1,12,1)

day = st.number_input("Day",1,31,1)

quarter = st.number_input("Quarter",1,4,1)

customer_age = st.number_input("Customer Age",18,80,30)

customer_gender = st.selectbox("Customer Gender",["Male","Female"])

country = st.selectbox(
    "Country",
    ["India","United States","Germany","France","UK","UAE"]
)

customer_segment = st.selectbox(
    "Customer Segment",
    ["New","Returning","Loyal","Premium"]
)

product_category = st.selectbox(
    "Product Category",
    ["Electronics","Fashion","Beauty","Books","Sports","Home"]
)

unit_price = st.number_input("Unit Price",0.0)

quantity = st.number_input("Quantity",1)

discount = st.number_input("Discount Percent",0.0)

shipping_cost = st.number_input("Shipping Cost",0.0)

order_amount = st.number_input("Order Amount",0.0)

review = st.slider("Review Rating",1.0,5.0,4.0)

delivery = st.number_input("Delivery Days",1)

# ----------------------------
# Simple Encoding
# ----------------------------

gender = 1 if customer_gender=="Male" else 0

country_map={
"India":0,
"United States":1,
"Germany":2,
"France":3,
"UK":4,
"UAE":5
}

segment_map={
"New":0,
"Returning":1,
"Loyal":2,
"Premium":3
}

category_map={
"Electronics":0,
"Fashion":1,
"Beauty":2,
"Books":3,
"Sports":4,
"Home":5
}

# ----------------------------
# Prediction
# ----------------------------

if st.button("Predict"):

    sample = pd.DataFrame([[
        year,
        month,
        day,
        quarter,
        customer_age,
        gender,
        country_map[country],
        segment_map[customer_segment],
        category_map[product_category],
        unit_price,
        quantity,
        discount,
        shipping_cost,
        order_amount,
        review,
        delivery
    ]])

    sample = scaler.transform(sample)

    prediction = model.predict(sample)

    if prediction[0]==1:

        st.success("✅ High Value Order")

    else:

        st.error("❌ Normal Order")

# ----------------------------
# Footer
# ----------------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;'>
<h4>Developed by Abhay Mahajan</h4>
</div>
""",
unsafe_allow_html=True
)