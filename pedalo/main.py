from langchain.callbacks import StreamlitCallbackHandler
from pandas import DataFrame

from dotenv import load_dotenv
import os
import openai

from pedalo.agents import code_interpreter

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def run(
    prompt: str, df: DataFrame, st_callback: StreamlitCallbackHandler, openai_api_key: str, model="gpt-4"
):
    result = code_interpreter.run(prompt, df, st_callback, openai_api_key, model)
    return result


if __name__ == "__main__":
    run()
