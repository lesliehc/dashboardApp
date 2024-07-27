from io import StringIO
from openai import OpenAI
import csv
import streamlit as st
import pandas as pd
import os

def handle_input(choice):
    user_message = st.session_state.user_input if 'user_input' in st.session_state else None
    if user_message:
        df = create_chatgpt_prompt(user_message)
        st.write(df)
        option_converter(df, choice)

def create_chatgpt_prompt(user_prompt:str):
    prompt = f"""
    {user_prompt}
    """
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the generated content
    generated_content = completion.choices[0].message.content
    st.write(generated_content)

def process_file(uploaded_file):
    if uploaded_file is not None:
        # Check the file extension and process accordingly
        if uploaded_file.name.endswith('.csv'):
            # Assuming the uploaded file is a CSV, load it into a DataFrame
            df = pd.read_csv(uploaded_file)
            # Display the DataFrame
            return df
        elif uploaded_file.name.endswith('.xlsx'):
            # If Excel, load with the corresponding function
            df = pd.read_excel(uploaded_file)
            return df
        else:
            # If it's neither CSV nor XLSX, just display a simple file read (works for text files)
            content = uploaded_file.getvalue()
            st.text(content.decode("utf-8"))

def option_converter(uploaded_file_df:pd.DataFrame,choice:str):
    if choice == 'Table':
        st.write("You chose Table.")
        st.table(uploaded_file_df)
    elif choice == 'Line Chart':
        st.write("You chose Line Chart.")
        st.line_chart(uploaded_file_df)
    elif choice == 'Bar Chart':
        st.write("You chose Bar Chart.")
        st.bar_chart(uploaded_file_df)

def main():

    api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)
    st.title("Dashboards")

    options = ['Table', 'Line Chart', 'Bar Chart']

    # Radio buttons to select one of the options
    choice = st.radio("Choose one option:", options, index=0)

    # Display the selected option
    st.write(f'You selected: {choice}')

    st.text_input("Type your message:", key='user_input', on_change=handle_input(choice))
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx', 'txt'])

    if uploaded_file is not None:
        # Call function when a file is uploaded
        file_df = process_file(uploaded_file)
        option_converter(file_df,choice)

if __name__ == "__main__":
    main()