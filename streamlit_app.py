import streamlit as st
import pandas as pd
 
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
        st.write("reading score is ", reading_score)
        st.write("writing score is ", writing_score)
        st.write("You selected:", gender)
        st.write("You selected:", race_ethnicity)
        st.write("You selected:", parental_level_of_education)
        st.write("You selected:", lunch)
        st.write("You selected:", test_preparation_course)
        st.write("Submitted")
    


#  data=CustomData(
#             gender=request.form.get('gender'),
#             race_ethnicity=request.form.get('ethnicity'),
#             parental_level_of_education=request.form.get('parental_level_of_education'),
#             lunch=request.form.get('lunch'),
#             test_preparation_course=request.form.get('test_preparation_course'),
#             reading_score=float(request.form.get('writing_score')),
#             writing_score=float(request.form.get('reading_score'))

#         )
#         pred_df=data.get_data_as_data_frame()
#         print(pred_df)
#         print("Before Prediction")

#         predict_pipeline=PredictPipeline()
#         print("Mid Prediction")
#         results=predict_pipeline.predict(pred_df)
#         print("after Prediction")
#         return render_template('home.html',results=results[0])