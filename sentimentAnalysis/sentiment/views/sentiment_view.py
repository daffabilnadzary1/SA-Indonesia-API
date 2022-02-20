import streamlit as st
# import sys 
# sys.path.append("/sentiment/controller/")
from .api import predicting

st.title("My first app created in streamlit")

with st.form("my_form"):
    # st.write("Inside the form")
    # slider_val = st.slider("Form slider")
    # checkbox_val = st.checkbox("Form checkbox")

    # # Every form must have a submit button.
    # submitted = st.form_submit_button("Submit")
    # if submitted:
    #     st.write("slider", slider_val, "checkbox", checkbox_val)

    text = st.text_input("Insert Your Sentiment Here")
    bt_predict = st.form_submit_button("Predict")
    if bt_predict:
        prediction = predicting(text)
        st.text("Results:")
        st.json(prediction)
        