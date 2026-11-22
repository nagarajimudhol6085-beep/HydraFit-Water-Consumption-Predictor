# 💧 HydraFit – Daily Water Consumption Predictor

## 📌 Project Overview
HydraFit is a machine learning web application that estimates daily plain-water consumption based on personal and body measurements.

The project uses the NHANES 2021–2023 dataset and a Linear Regression model deployed through Streamlit.

## 🚀 Features
- Predicts reported daily plain-water consumption.
- Accepts age, gender, height, weight, waist and hip measurements, and household size.
- Calculates Body Mass Index (BMI).
- Provides a simple, user-friendly Streamlit interface.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib and Seaborn (EDA)

## 🤖 Machine Learning Algorithms Tested
1. Linear Regression
2. Decision Tree Regression
3. K-Nearest Neighbors (KNN)
4. Support Vector Regression (SVR)

## 📊 Final Model Performance

**Selected Model:** Linear Regression (7 features)

| Metric | Result |
|---|---|
| MAE | 827.43 g |
| RMSE | 1162.47 g |
| R² Score | 0.0665 |

The final model uses median imputation and feature scaling through a Scikit-learn pipeline.

## 📂 Project Structure

```text
HydraFit/
├── app.py
├── hydrafit_model.pkl
└── requirements.txt
```

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app.py
```

## ⚠️ Limitations
The model predicts reported plain-water consumption, not an individual's recommended daily water requirement.

The model has limited predictive accuracy and is intended for educational and experimental purposes only.

## 🎯 Project Objective
To demonstrate an end-to-end machine learning workflow, including data collection, preprocessing, exploratory data analysis, model comparison, evaluation, and web application deployment.
