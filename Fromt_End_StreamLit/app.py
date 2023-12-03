import streamlit as st
import pandas as pd
import pickle

# Load the pickle file
model_filename = "V2_M1.pkl"
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Encoding mappings
encoding_mappings = {
    'school': {'GP': 0, 'LVA': 1, 'MS': 2, 'SLA': 3},
    'address': {'R': 0, 'U': 1},
    'guardian': {'father': 0, 'mother': 1, 'other': 2},
    'paid': {'no': 0, 'yes': 1},
    'higher': {'no': 0, 'yes': 1},
}

# Function to preprocess input data
def preprocess_input(data):
    # Encode categorical variables
    for column, mapping in encoding_mappings.items():
        if column in data.columns:
            data[column] = data[column].map(mapping)

    # Add any additional preprocessing steps if needed
    return data

# Function to make predictions
def predict_output(input_data):
    input_data = preprocess_input(input_data)
    prediction = model.predict(input_data)
    return round(prediction[0])

# Streamlit app
def main():
     
    st.markdown(
        """
        <style>
            body {
                background-image: url("file:C:\\Users\\surya\\hackverse\\studphoto.jpg");
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("Student Performance Prediction App")

    # Input variables
    school = st.selectbox("School", ['GP', 'MS', "LVA", "SLA"])
    address = st.selectbox("Address", ['R', 'U'])
    Medu = st.slider("Mother's Education", 0, 4, 2)
    Fedu = st.slider("Father's Education", 0, 4, 2)
    guardian = st.selectbox("Guardian", ['father', 'mother', 'other'])
    traveltime = st.slider("Travel Time", 1, 4, 2)
    failures = st.slider("Number of Failures", 0, 4, 0)
    paid = st.selectbox("Extra Paid Classes", ['yes', 'no'])
    higher = st.selectbox("Wants to Take Higher Education", ['yes', 'no'])
    famrel = st.slider("Family Relationship", 1, 5, 3)
    freetime = st.slider("Free Time", 1, 5, 3)
    goout = st.slider("Go Out", 1, 5, 3)
    absences = st.slider("Number of School Absences", 0, 93, 0)
    G1 = st.slider("Grade G1", 0, 20, 10)
    G2 = st.slider("Grade G2", 0, 20, 10)

    # Create a dictionary with input data
    input_data = {
        'school': school,
        'address': address,
        'Medu': Medu,
        'Fedu': Fedu,
        'guardian': guardian,
        'traveltime': traveltime,
        'failures': failures,
        'paid': paid,
        'higher': higher,
        'famrel': famrel,
        'freetime': freetime,
        'goout': goout,
        'absences': absences,
        'G1': G1,
        'G2': G2,
    }

    # Convert input data to a DataFrame for preprocessing
    input_df = pd.DataFrame([input_data])

    # Make prediction
    prediction = predict_output(input_df)

    # Display the prediction inside a box
    st.subheader("Predicted Final Grade (G3): ")
    st.success(f"The predicted final grade is: {prediction}")

if __name__ == "__main__":
    main()
