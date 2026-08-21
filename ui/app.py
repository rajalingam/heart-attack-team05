import streamlit as st
import requests


# ============================================================
# Configuration
# ============================================================

API_URL = "http://heart-disease-api:8000/predict"


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Heart Disease Risk Predictor",
    page_icon="❤️",
    layout="wide"
)


# ============================================================
# Header
# ============================================================

st.title("❤️ Heart Disease Risk Predictor")

st.markdown(
    """
    Enter the information below to estimate the heart disease
    risk predicted by the machine-learning model.
    """
)

st.warning(
    "⚠️ This application is for educational/project demonstration "
    "purposes only. It is not a medical diagnosis."
)


# ============================================================
# STEP 1 - BASIC INFORMATION
# ============================================================

st.header("👤 1. Basic Information")

col1, col2, col3 = st.columns(3)

with col1:

    state = st.selectbox(
        "State",
        [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Other"
        ]
    )

with col2:

    sex = st.selectbox(
        "Sex",
        [
            "Female",
            "Male"
        ]
    )

with col3:

    age_category = st.selectbox(
        "Age Category",
        [
            "Age 18 to 24",
            "Age 25 to 29",
            "Age 30 to 34",
            "Age 35 to 39",
            "Age 40 to 44",
            "Age 45 to 49",
            "Age 50 to 54",
            "Age 55 to 59",
            "Age 60 to 64",
            "Age 65 to 69",
            "Age 70 to 74",
            "Age 75 to 79",
            "Age 80 or older"
        ]
    )


# ============================================================
# HEIGHT / WEIGHT / BMI
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    height = st.number_input(
        "Height (meters)",
        min_value=0.5,
        max_value=2.5,
        value=1.70,
        step=0.01
    )

with col2:

    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=300.0,
        value=70.0,
        step=0.1
    )

with col3:

    # Automatically calculate BMI
    if height > 0:
        bmi = weight / (height ** 2)
    else:
        bmi = 0.0

    # Read-only BMI display
    st.metric(
        label="BMI (Calculated)",
        value=f"{bmi:.2f}"
    )


# ============================================================
# STEP 2 - HEALTH INFORMATION
# ============================================================

st.divider()

st.header("🏥 2. Health Information")


col1, col2, col3 = st.columns(3)


with col1:

    general_health = st.selectbox(
        "General Health",
        [
            "Excellent",
            "Very good",
            "Good",
            "Fair",
            "Poor"
        ]
    )

    physical_health_days = st.number_input(
        "Physical Health Days",
        min_value=0,
        max_value=30,
        value=0
    )

    mental_health_days = st.number_input(
        "Mental Health Days",
        min_value=0,
        max_value=30,
        value=0
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0,
        max_value=24,
        value=7
    )


with col2:

    had_angina = st.selectbox(
        "Had Angina",
        ["No", "Yes"]
    )

    had_stroke = st.selectbox(
        "Had Stroke",
        ["No", "Yes"]
    )

    had_asthma = st.selectbox(
        "Had Asthma",
        ["No", "Yes"]
    )

    had_copd = st.selectbox(
        "Had COPD",
        ["No", "Yes"]
    )


with col3:

    had_skin_cancer = st.selectbox(
        "Had Skin Cancer",
        ["No", "Yes"]
    )

    had_depressive_disorder = st.selectbox(
        "Had Depressive Disorder",
        ["No", "Yes"]
    )

    had_kidney_disease = st.selectbox(
        "Had Kidney Disease",
        ["No", "Yes"]
    )

    had_arthritis = st.selectbox(
        "Had Arthritis",
        ["No", "Yes"]
    )


# Diabetes separately

had_diabetes = st.selectbox(
    "Had Diabetes",
    [
        "No",
        "Yes",
        "Yes, but only during pregnancy",
        "No, borderline diabetes",
        "Yes, borderline diabetes"
    ]
)


# ============================================================
# STEP 3 - LIFESTYLE
# ============================================================

st.divider()

st.header("🏃 3. Lifestyle")


col1, col2, col3 = st.columns(3)


with col1:

    physical_activities = st.selectbox(
        "Physical Activities",
        ["Yes", "No"]
    )

    smoker_status = st.selectbox(
        "Smoking Status",
        [
            "Never smoked",
            "Former smoker",
            "Current smoker - now smokes some days",
            "Current smoker - now smokes every day"
        ]
    )


with col2:

    ecigarette_usage = st.selectbox(
        "E-Cigarette Usage",
        [
            "Never used e-cigarettes in my entire life",
            "Not at all (right now)",
            "Use them some days",
            "Use them every day"
        ]
    )

    alcohol_drinkers = st.selectbox(
        "Alcohol Drinkers",
        ["No", "Yes"]
    )


with col3:

    chest_scan = st.selectbox(
        "Chest Scan",
        ["No", "Yes"]
    )

    high_risk_last_year = st.selectbox(
        "High Risk Last Year",
        ["No", "Yes"]
    )


# ============================================================
# STEP 4 - DAILY ACTIVITIES / FUNCTIONAL HEALTH
# ============================================================

st.divider()

st.header("🧠 4. Daily Activities & Functional Health")


col1, col2, col3 = st.columns(3)


with col1:

    deaf_or_hard_of_hearing = st.selectbox(
        "Deaf or Hard of Hearing",
        ["No", "Yes"]
    )

    blind_or_vision_difficulty = st.selectbox(
        "Blind or Vision Difficulty",
        ["No", "Yes"]
    )


with col2:

    difficulty_concentrating = st.selectbox(
        "Difficulty Concentrating",
        ["No", "Yes"]
    )

    difficulty_walking = st.selectbox(
        "Difficulty Walking",
        ["No", "Yes"]
    )


with col3:

    difficulty_dressing_bathing = st.selectbox(
        "Difficulty Dressing/Bathing",
        ["No", "Yes"]
    )

    difficulty_errands = st.selectbox(
        "Difficulty Doing Errands",
        ["No", "Yes"]
    )


# ============================================================
# REMOVED TEETH
# ============================================================

removed_teeth = st.selectbox(
    "Removed Teeth",
    [
        "None of them",
        "1 to 5",
        "6 or more, but not all",
        "All"
    ]
)


# ============================================================
# STEP 5 - PREVENTIVE CARE
# ============================================================

st.divider()

st.header("💉 5. Preventive Care & Other Information")


col1, col2, col3 = st.columns(3)


with col1:

    last_checkup = st.selectbox(
        "Last Checkup",
        [
            "Within past year (anytime less than 12 months ago)",
            "Within past 2 years",
            "Within past 5 years",
            "5 or more years ago"
        ]
    )

    flu_vax = st.selectbox(
        "Flu Vaccine in Last 12 Months",
        ["No", "Yes"]
    )


with col2:

    pneumo_vax = st.selectbox(
        "Pneumonia Vaccine Ever",
        ["No", "Yes"]
    )

    tetanus = st.selectbox(
        "Tetanus Vaccine Last 10 Years",
        [
            "Yes, received Tdap",
            "Yes, received tetanus but not Tdap",
            "Yes, received Tdap within 10 years",
            "No",
            "Don't know"
        ]
    )


with col3:

    hiv_testing = st.selectbox(
        "HIV Testing",
        ["No", "Yes"]
    )

    covid_pos = st.selectbox(
        "COVID-19 Positive",
        [
            "No",
            "Yes",
            "Tested positive using home test",
            "Tested positive using laboratory test"
        ]
    )


# ============================================================
# RACE / ETHNICITY
# ============================================================

race_ethnicity = st.selectbox(
    "Race / Ethnicity",
    [
        "White only, Non-Hispanic",
        "Black only, Non-Hispanic",
        "Other"
    ]
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "❤️ Predict Heart Disease Risk",
    type="primary",
    use_container_width=True
)


# ============================================================
# CREATE PAYLOAD
# ============================================================

if predict_button:

    payload = {

        # Basic
        "State": state,
        "Sex": sex,
        "AgeCategory": age_category,

        # Health
        "GeneralHealth": general_health,
        "PhysicalHealthDays": physical_health_days,
        "MentalHealthDays": mental_health_days,
        "LastCheckupTime": last_checkup,
        "PhysicalActivities": physical_activities,
        "SleepHours": sleep_hours,

        # Physical
        "RemovedTeeth": removed_teeth,

        # Disease history
        "HadAngina": had_angina,
        "HadStroke": had_stroke,
        "HadAsthma": had_asthma,
        "HadSkinCancer": had_skin_cancer,
        "HadCOPD": had_copd,
        "HadDepressiveDisorder": had_depressive_disorder,
        "HadKidneyDisease": had_kidney_disease,
        "HadArthritis": had_arthritis,
        "HadDiabetes": had_diabetes,

        # Functional
        "DeafOrHardOfHearing": deaf_or_hard_of_hearing,
        "BlindOrVisionDifficulty": blind_or_vision_difficulty,
        "DifficultyConcentrating": difficulty_concentrating,
        "DifficultyWalking": difficulty_walking,
        "DifficultyDressingBathing": difficulty_dressing_bathing,
        "DifficultyErrands": difficulty_errands,

        # Lifestyle
        "SmokerStatus": smoker_status,
        "ECigaretteUsage": ecigarette_usage,

        # Other
        "ChestScan": chest_scan,
        "RaceEthnicityCategory": race_ethnicity,

        # Measurements
        "HeightInMeters": height,
        "WeightInKilograms": weight,
        "BMI": round(bmi, 2),

        # Prevention
        "AlcoholDrinkers": alcohol_drinkers,
        "HIVTesting": hiv_testing,
        "FluVaxLast12": flu_vax,
        "PneumoVaxEver": pneumo_vax,
        "TetanusLast10Tdap": tetanus,

        # Risk / COVID
        "HighRiskLastYear": high_risk_last_year,
        "CovidPos": covid_pos
    }


    # ========================================================
    # Show Payload for Debugging
    # ========================================================

    with st.expander("🔍 View request data"):

        st.json(payload)


    # ========================================================
    # Call FastAPI
    # ========================================================

    with st.spinner(
        "Calling heart disease prediction service..."
    ):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    "Prediction completed successfully!"
                )

                st.divider()

                st.header("❤️ Prediction Result")

                st.json(result)

            else:

                st.error(
                    f"Prediction failed: {response.text}"
                )

        except requests.exceptions.RequestException as e:

            st.error(
                f"Unable to connect to FastAPI: {e}"
            )