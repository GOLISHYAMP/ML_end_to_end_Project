import streamlit as st
import pandas as pd

from src.pipeline import predict_pipeline
 
st.write("""
# Predict Math Score
""")


import streamlit as st

with st.form("my_form"):
    st.write("# Insert student info")
    reading_score = st.number_input("Insert a reading score", min_value=0, max_value=100, value="min")
    writing_score = st.number_input("Insert a writing score", min_value=0, max_value=100, value="min")

    gender = st.selectbox(
        "Enter the Gender : ",
        ('female', 'male'),
    )

    race_ethnicity = st.selectbox(
        "Enter the race/ethnicity : ",
        ('group A', 'group B', 'group C', 'group D', 'group E'),
    )

    parental_level_of_education = st.selectbox(
        "Enter the parental level of education : ",
        ("bachelor's degree", 'some college', "master's degree", "associate's degree", 'high school', 'some high school'),
    )

    lunch = st.selectbox(
        "Enter the lunch : ",
        ('standard', 'free/reduced'),
    )

    test_preparation_course = st.selectbox(
        "Enter the test preparation course status : ",
        ('none', 'completed'),
    )

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        data=predict_pipeline.CustomData(
                    gender=gender,
                    race_ethnicity=race_ethnicity,
                    parental_level_of_education=parental_level_of_education,
                    lunch=lunch,
                    test_preparation_course=test_preparation_course,
                    reading_score=float(reading_score),
                    writing_score=float(writing_score)

                )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=predict_pipeline.PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        results=results[0]
        st.write("Predicted Math score is : ", results)
    


        