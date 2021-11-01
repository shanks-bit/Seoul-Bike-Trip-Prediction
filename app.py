from attr import attributes
import streamlit  as st
from model import predict_duration
import numpy as np

st.set_page_config(page_title="Seoul Bike Trip Duration Prediction App")

with st.form("prediction form"):
    st.header("Enter The Deciding Factors: ")

    distance = st.number_input("Distance: ", value=0, format="%d")
    havershine = st.number_input("Havershne: ")
    phour = st.slider("Pickup Hour: ", 0, 23, value=0, format="%d")
    pmin = st.slider("Pickup Minute: ", 0, 29, value=0, format="%d")
    dhour = st.slider("Droput Hour: ", 0, 23, value=0, format="%d")
    dmin = st.slider("Droput Minute: ", 0, 29, value=0, format="%d")
    temp = st.number_input("Temp: ")
    humid = st.number_input("Humid: ")
    solar = st.number_input("Solar: ")
    dust = st.number_input("Dust: ")

    submit_val = st.form_submit_button("Predict Duration")

if submit_val:
    # If Submit Is Pressed == TRUE
    attribute = np.array([distance,havershine,phour,pmin,dhour,
    dmin,temp,humid,solar,dust]).reshape(1,-1)

    if attribute.shape == (1,10):
        print("attributes valid")

        value = predict_duration(attributes=attribute)

        st.header("Here Are The Results: ")
        st.success(f"The Duration Prediction is {value} minutes.")



