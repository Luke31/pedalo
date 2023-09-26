from langchain.callbacks import StreamlitCallbackHandler
import streamlit as st
from pandas import DataFrame

from pedalo.main import run
import pandas as pd

# st.set_page_config(layout="wide")
st.title("PEDALO - Productive Exploratory Data Analysis using Langchain interrOgation")
st.write("Ask your data what you wanna know!")
model = st.sidebar.radio("Which model do you wanna use?", ("gpt-4", "gpt-3.5-turbo"), index=1)

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv"])



def run_df_analysis(prompt:str, df: DataFrame):
    st_callback = StreamlitCallbackHandler(st.container())
    response = run(prompt, df, st_callback, model)
    st.write(response)


def initial_analysis(df: DataFrame):
    run_df_analysis("Give a brief outline and interpretation of the file content.", df)


def user_interrogation(df: DataFrame):
    user_question = st.text_input("or enter your question about the CSV data:")
    if user_question:
        run_df_analysis(user_question, df)


def main():
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        # if st.button("Start analyzing"):
        st.write(f"Starting to analyze using model {model}...")
        if st.button("Give initial insight"):
            initial_analysis(df)
        user_interrogation(df)
    else:
        st.write("Please upload a CSV file.")

main()