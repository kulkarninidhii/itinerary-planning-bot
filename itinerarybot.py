import streamlit as st
import openai
import os
from openai import OpenAI

# Initialize your OpenAI API key
client = OpenAI(
api_key = os.getenv('OPENAI_API_KEY')
)
st.title('Itinerary Generator')

with st.sidebar:
    st.header("Plan Your Trip")
    # Inputs for generating an itinerary
    st.subheader("Input Your Trip Details")
    num_people = st.selectbox('Number of People', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=1)
    location = st.text_input('Location')
    num_days = st.selectbox('Number of Days', [1, 2, 3, 4, 5, 6, 7], index=3)
    ambience = st.selectbox('Ambience', ['Romantic', 'Adventure', 'Relaxation', 'Cultural', 'Party'])
    budget = st.slider('Budget in $', min_value=1000, max_value=10000, value=6000, step=500)
    st.subheader("Input Your Travel Dates")
    start_date = st.date_input("Start Date")

    submit_button = st.button('Generate Itinerary')

if submit_button:
    # Form the prompt to pass to ChatGPT
    prompt = f"Create a detailed itinerary for a trip with the following details: Number of People: {num_people}, Location: {location}, Number of Days: {num_days}, Ambience: {ambience}, Budget: ${budget} and Travel Dates: ${start_date}. Include day-wise activities. Write a short recommendation according to the weather."

    # Make the request to OpenAI's API
    response = client.completions.create(
      model="gpt-3.5-turbo-instruct", 
      prompt=prompt,
      temperature=0.5,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    # Display the generated itinerary
    st.header("Your Custom Itinerary")
    st.write(response.choices[0].text)
else:
    # Display the inputs for confirmation before submission
    st.header("Your Trip Details")
    st.write(f"Number of People: {num_people}")
    st.write(f"Location: {location}")
    st.write(f"Number of Days: {num_days}")
    st.write(f"Ambience: {ambience}")
    st.write(f"Budget: ${budget}")

