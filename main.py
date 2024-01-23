import streamlit as st
import pickle5 as pickle

# Load the trained model
countVector  =pickle.load(open("count_vectorizer.pkl","rb"))
model = pickle.load(open('model.pkl', 'rb'))  # Replace with your trained model

# Application Frontend

# Title of the Application
st.title('Spam Classifier')

# Text Input for the user
text_input = st.text_area("Enter the text to classify:", "")

# Classification Program
if st.button('Classify'):
    # Perform the classification
    vector  = countVector.transform([text_input])
    prediction = model.predict(vector)[0]

    # Display the result
    if prediction == 1:
        st.write("This text is SPAM.")
    else:
        st.write("This text is NOT SPAM.")
