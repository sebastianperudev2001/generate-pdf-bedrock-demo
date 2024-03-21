import streamlit as st
import requests
from langchain.prompts import PromptTemplate
import json

st.title("Text Summarizer")

# Input field for user question
user_input = st.text_area("Enter your text here:", height=200)

# Button to submit the question
submit_button = st.button("Submit")

if submit_button and user_input:

    user_input = user_input.replace("\n", " ")

    # Define API endpoint URL
    url = "https://qe0nvuo011.execute-api.us-east-1.amazonaws.com/dev"

    # Send POST request with user question


    prompt = PromptTemplate.from_template(
        "Summarize the following text into 2 bullet points.Text: {langchain_input}. Output Format: JSON file which contains an array of objects with the following schema per object: id_number, content "
        )
    

    prompt = prompt.format(langchain_input=user_input)
    params = {
        "prompt": prompt  # Replace with your prompt value
    }
    response = requests.post(url, params=params)

    # Parse JSON response
    if response.status_code == 200:
        bedrock_response = response.json()['body']
        # Create a JSON file locally to store the JSON body response
        with open('response.json', 'w') as file:
            json.dump(response.json(), file)
                 
        start_index = bedrock_response.find("```json") + len("```json")
        print("PRIMER BIEN")
        end_index = bedrock_response.find("```", start_index)
        print("SEGUNDO BIEN")
        json_data = bedrock_response[start_index:end_index]
        print(json_data)
        print("TERCER BIEN")
        json_string = json_data.replace("\\n", "").replace("\\", "")
        print("CUARTO BIEN")
        parsed_json = json.loads(json_string)
        print("QUINTO BIEN")

        bullet_points = ""
        for item in parsed_json:
            content = item.get("content")
            bullet_points += f"- {content}\n"
        
        st.markdown("### Summary:")
        st.markdown(bullet_points)
        
    else:
        st.markdown("### Error:")
        st.text_area(response)
        st.error("Error: Failed to get response from API")
