import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="HydraFit",
    page_icon="💧",
    layout="centered"
)

# -----------------------------------------
# CUSTOM CSS
# -----------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0c4a6e 0%,
            #075985 50%,
            #082f49 100%
        );
        color: #ffffff !important;
    }

    /* Main container */
    .block-container {
        max-width: 750px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* All headings */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }

    /* General text */
    .stApp p,
    .stApp label,
    .stApp span {
        color: #ffffff !important;
    }

    /* Form labels */
    [data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
        font-weight: 500;
    }

    /* Form background */
    [data-testid="stForm"] {
        background-color: rgba(15, 23, 42, 0.45);
        padding: 25px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.2);
    }

    /* Number input boxes */
    [data-testid="stNumberInput"] input {
        background-color: #1e3a5f !important;
        color: #ffffff !important;
        border-radius: 8px;
    }

    /* Number input container */
    [data-testid="stNumberInput"] [data-baseweb="input"] {
        background-color: #1e3a5f !important;
    }

    /* Number input buttons */
    [data-testid="stNumberInput"] button {
        background-color: #1e3a5f !important;
        color: white !important;
    }

    /* Dropdown */
    [data-baseweb="select"] > div {
        background-color: #1e3a5f !important;
        color: #ffffff !important;
        border-radius: 8px;
    }

    /* Dropdown text */
    [data-baseweb="select"] span {
        color: #ffffff !important;
    }

    /* Prediction button */
    div.stFormSubmitButton > button {
        background-color: #0284c7 !important;
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        font-weight: 700;
        width: 100%;
        transition: 0.3s;
    }

    /* Button hover */
    div.stFormSubmitButton > button:hover {
        background-color: #0369a1 !important;
        color: #ffffff !important;
        border: 1px solid #38bdf8;
    }

    /* Button text */
    div.stFormSubmitButton > button p {
        color: #ffffff !important;
    }

    /* Result card */
    .result-box {
        background: linear-gradient(
            135deg,
            #0284c7,
            #0369a1
        );
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        color: #ffffff !important;
        margin-top: 25px;
        border: 1px solid #7dd3fc;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }

    /* Result heading */
    .result-box h3 {
        color: #ffffff !important;
        font-size: 22px;
    }

    /* Result number */
    .result-number {
        font-size: 46px;
        font-weight: 800;
        color: #ffffff !important;
        margin: 15px 0;
    }

    /* Result paragraph */
    .result-box p {
        color: #ffffff !important;
    }

    /* BMI metric */
    [data-testid="stMetric"] {
        background-color: rgba(15, 23, 42, 0.45);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.2);
    }

    [data-testid="stMetricLabel"] p,
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    /* Captions */
    [data-testid="stCaptionContainer"] p {
        color: #ffffff !important;
        opacity: 0.9;
    }

    /* Information box */
    [data-testid="stAlert"] {
        background-color: #164e63 !important;
        border-radius: 10px;
    }

    [data-testid="stAlert"] p {
        color: #ffffff !important;
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,0.25);
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# LOAD MODEL
# -----------------------------------------

MODEL_PATH = Path(__file__).resolve().parent / "hydrafit_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()

except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()


# -----------------------------------------
# APP HEADER
# -----------------------------------------

st.title("💧 HydraFit")

st.markdown("### Daily Water Consumption Predictor")

st.write(
    "Estimate reported daily plain-water consumption "
    "using Machine Learning."
)

st.divider()


# -----------------------------------------
# USER INPUT FORM
# -----------------------------------------

st.subheader("👤 Enter Your Details")

with st.form("water_form"):

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=80,
            value=25
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        height = st.number_input(
            "Height (cm)",
            min_value=120.0,
            max_value=220.0,
            value=170.0
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=30.0,
            max_value=250.0,
            value=70.0
        )

    with col2:

        waist = st.number_input(
            "Waist (cm)",
            min_value=50.0,
            max_value=200.0,
            value=85.0
        )

        hip = st.number_input(
            "Hip (cm)",
            min_value=60.0,
            max_value=220.0,
            value=100.0
        )

        household = st.number_input(
            "Household Size",
            min_value=1,
            max_value=7,
            value=3
        )

    predict_button = st.form_submit_button(
        "💧 Predict Water Consumption",
        use_container_width=True
    )


# -----------------------------------------
# PREDICTION
# -----------------------------------------

if predict_button:

    gender_code = 1 if gender == "Male" else 2

    input_data = pd.DataFrame([{
        "RIDAGEYR": age,
        "RIAGENDR": gender_code,
        "BMXHT": height,
        "BMXWT": weight,
        "BMXWAIST": waist,
        "BMXHIP": hip,
        "DMDHHSIZ": household
    }])

    prediction = model.predict(input_data)[0]

    prediction = max(0, prediction)

    water_litres = prediction / 1000

    bmi = weight / ((height / 100) ** 2)

    # Prediction result
    st.markdown(f"""
    <div class="result-box">

        <h3>Estimated Daily Water Consumption</h3>

        <div class="result-number">
            💧 {water_litres:.2f} Litres
        </div>

        <p>
            Approximately {prediction:.0f} grams
            of plain water
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # BMI
    st.metric(
        "Your Body Mass Index (BMI)",
        f"{bmi:.1f}"
    )

    st.info(
        "This is an experimental prediction of reported "
        "water consumption, not a recommended daily "
        "water intake. The model has limited accuracy."
    )


# -----------------------------------------
# FOOTER
# -----------------------------------------

st.divider()

st.caption(
    "💧 HydraFit | Built with Python, Machine Learning & Streamlit"
)