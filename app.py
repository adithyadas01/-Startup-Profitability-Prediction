# import streamlit as st
# import pickle
# import pandas as pd

# # ================================
# #  Load Model + Encoders
# # ================================
# model = pickle.load(open("best_model.pkl", "rb"))
# encoders = pickle.load(open("encoders.pkl", "rb"))

# # ================================
# #  Background Image
# # ================================
# background_image = r"C:\Users\ADITHYA\OneDrive\Desktop\START_UP_PREDICTION_PROJECT\1679747717744.png"

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] {{
# background-image: url("file:///{background_image}");
# background-size: cover;
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}
# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)

# # ================================
# #  Page Title
# # ================================
# st.title("🚀 Startup Profitability Prediction")
# st.success("Model Loaded Successfully!")
# st.write("### Enter the Startup Details Below")

# # ================================
# # DROPDOWN OPTIONS
# # ================================
# startup_names = list(encoders["Startup Name"].classes_) if "Startup Name" in encoders else ["Startup_1","Startup_2","Startup_3","Startup_4","Startup_5"]
# industries = list(encoders["Industry"].classes_) if "Industry" in encoders else ["IoT","EdTech","Gaming"]
# regions = list(encoders["Region"].classes_) if "Region" in encoders else ["Europe","South America"]
# exit_statuses = list(encoders["Exit Status"].classes_) if "Exit Status" in encoders else ["Private","Acquired"]

# # ================================
# # INPUTS (match training features)
# # ================================
# startup_name = st.selectbox("Startup Name", startup_names)
# industry = st.selectbox("Industry", industries)
# region = st.selectbox("Region", regions)
# exit_status = st.selectbox("Exit Status", exit_statuses)

# funding_rounds = st.number_input("Funding Rounds", min_value=0, format="%d")
# funding_amount = st.number_input("Funding Amount (M USD)", min_value=0.0, format="%.2f")
# valuation = st.number_input("Valuation (M USD)", min_value=0.0, format="%.2f")
# revenue = st.number_input("Revenue (M USD)", min_value=0.0, format="%.2f")
# employees = st.number_input("Employees", min_value=0, format="%d")
# market_share = st.number_input("Market Share (%)", min_value=0.0, format="%.2f")
# year_founded = st.number_input("Year Founded", min_value=1900, max_value=2025, format="%d")

# # ================================
# # PREDICTION
# # ================================
# if st.button("Predict Profitability"):
#     # Encode categorical data
#     startup_name_enc = encoders["Startup Name"].transform([startup_name])[0] if "Startup Name" in encoders else startup_names.index(startup_name)
#     industry_enc = encoders["Industry"].transform([industry])[0] if "Industry" in encoders else industries.index(industry)
#     region_enc = encoders["Region"].transform([region])[0] if "Region" in encoders else regions.index(region)
#     exit_status_enc = encoders["Exit Status"].transform([exit_status])[0] if "Exit Status" in encoders else exit_statuses.index(exit_status)

#     # Create final input for model (all features used during training)
#     input_df = pd.DataFrame([[
#         startup_name_enc,
#         industry_enc,
#         funding_rounds,
#         funding_amount,
#         valuation,
#         revenue,
#         employees,
#         market_share,
#         year_founded,
#         region_enc,
#         exit_status_enc
#     ]], columns=[
#         "Startup Name",
#         "Industry",
#         "Funding Rounds",
#         "Funding Amount (M USD)",
#         "Valuation (M USD)",
#         "Revenue (M USD)",
#         "Employees",
#         "Market Share (%)",
#         "Year Founded",
#         "Region",
#         "Exit Status"
#     ])

#     # Predict
#     prediction = model.predict(input_df)[0]

#     # Output
#     if prediction == 1:
#         st.success("🎉 This Startup is Profitable!")
#     else:
#         st.error("⚠ This Startup is Not Profitable.")

import streamlit as st
import pickle
import pandas as pd
import base64

# ================================
#  Load Model + Encoders
# ================================
model = pickle.load(open("best_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

# ================================
#  Background Image Function
# ================================
def set_background(png_file):
    """
    Sets background image from a local file
    """
    with open(png_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set your background
background_image = r"C:\Users\ADITHYA\OneDrive\Desktop\START_UP_PREDICTION_PROJECT\WhatsApp Image 2025-12-01 at 19.41.15_1cc9f068.jpg"
set_background(background_image)

# ================================
#  Page Title
# ================================
st.title("🚀 Startup Profitability Prediction")
st.success("Model Loaded Successfully!")
st.write("### Enter the Startup Details Below")

# ================================
#  DROPDOWN OPTIONS
# ================================
startup_names = list(encoders["Startup Name"].classes_) if "Startup Name" in encoders else ["Startup_1","Startup_2","Startup_3","Startup_4","Startup_5"]
industries = list(encoders["Industry"].classes_) if "Industry" in encoders else ["IoT","EdTech","Gaming"]
regions = list(encoders["Region"].classes_) if "Region" in encoders else ["Europe","South America"]
exit_statuses = list(encoders["Exit Status"].classes_) if "Exit Status" in encoders else ["Private","Acquired"]

# ================================
# INPUTS (match training features)
# ================================
startup_name = st.selectbox("Startup Name", startup_names)
industry = st.selectbox("Industry", industries)
region = st.selectbox("Region", regions)
exit_status = st.selectbox("Exit Status", exit_statuses)

funding_rounds = st.number_input("Funding Rounds", min_value=0, format="%d")
funding_amount = st.number_input("Funding Amount (M USD)", min_value=0.0, format="%.2f")
valuation = st.number_input("Valuation (M USD)", min_value=0.0, format="%.2f")
revenue = st.number_input("Revenue (M USD)", min_value=0.0, format="%.2f")
employees = st.number_input("Employees", min_value=0, format="%d")
market_share = st.number_input("Market Share (%)", min_value=0.0, format="%.2f")
year_founded = st.number_input("Year Founded", min_value=1900, max_value=2025, format="%d")

# ================================
# PREDICTION
# ================================
if st.button("Predict Profitability"):
    # Encode categorical data
    startup_name_enc = encoders["Startup Name"].transform([startup_name])[0] if "Startup Name" in encoders else startup_names.index(startup_name)
    industry_enc = encoders["Industry"].transform([industry])[0] if "Industry" in encoders else industries.index(industry)
    region_enc = encoders["Region"].transform([region])[0] if "Region" in encoders else regions.index(region)
    exit_status_enc = encoders["Exit Status"].transform([exit_status])[0] if "Exit Status" in encoders else exit_statuses.index(exit_status)

    # Create final input for model (all features used during training)
    input_df = pd.DataFrame([[ 
        startup_name_enc,
        industry_enc,
        funding_rounds,
        funding_amount,
        valuation,
        revenue,
        employees,
        market_share,
        year_founded,
        region_enc,
        exit_status_enc
    ]], columns=[
        "Startup Name",
        "Industry",
        "Funding Rounds",
        "Funding Amount (M USD)",
        "Valuation (M USD)",
        "Revenue (M USD)",
        "Employees",
        "Market Share (%)",
        "Year Founded",
        "Region",
        "Exit Status"
    ])

    # Predict
    prediction = model.predict(input_df)[0]

    # Output
    if prediction == 1:
        st.success("🎉 This Startup is Profitable!")
    else:
        st.error("⚠ This Startup is Not Profitable.")
