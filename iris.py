import streamlit as st
import joblib
from sklearn.datasets import load_iris

iris = load_iris()

st.title("Iris Flower Classifier")

sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

try:
    model = joblib.load("iris_classifier_knn.joblib")
    model_loaded = True
except Exception as e:
    st.error(f"⚠️ Unable to load the model: {e}")
    model_loaded = False

if st.button("Predict Flower"):
    if model_loaded:
        try:
            sample = [[sepal_length, sepal_width, petal_length, petal_width]]
            prediction = model.predict(sample)[0]
            flower_name = iris.target_names[prediction]
            st.success(f"🌸 Predicted flower: **{flower_name}**")
        except Exception as e:
            st.error(f"❌ Prediction error: {e}")
    else:
        st.warning("Prediction unavailable. Please ensure the model file is present and valid.")
