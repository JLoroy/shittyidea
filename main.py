## OPENAI part
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

system_prompt_template = """
    You are a idea examinator. Your job is to critize and point all the problems and flaws of the idea you've been presented.
    You've done this job for 30 years and you are now a old, angry guy which takes nothing seriously. 
    All your comments are very sarcastic, you don't want to be bothered anymore. You are mean, disrespectful.
    Your comments are always exagerated and hyperbollistic. You have a lot of humor.
"""

ai_prompt_template = "Oh god, here's another one. I cannot believe how ridiculous their idea is. This must be the worst idea a basic human brain can produce. This is so stupid. Well, if you think you have such a great idea, why don't you tell me about it?"

human_prompt_template = """Here's my idea: {description}"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt_template)
ai_message_prompt = AIMessagePromptTemplate.from_template(ai_prompt_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_prompt_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, ai_message_prompt, human_message_prompt])

def load_Chat():
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)
    return chat

chat = load_Chat()



#### Streamlit Part
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Tell me about your shitty idea", page_icon=":poop:")

col1, col2 = st.columns(2)
def get_description():
    input_description = st.text_area(label="Description", placeholder="So I have this great idea...", key="description_input")
    return input_description
with col1:
    st.header("Challenge your shitty idea")
    st.markdown("If you think you have such a great idea, why don't you tell me about it?")
    input_description = get_description()

dickhead = Image.open('dickhead.png')
with col2:
    st.image(dickhead,use_column_width='always')

st.markdown("This tool will challenge and destroy your ideas, in an humoristic way hopefully. \
            Made with [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) \
            Image was done using StableDiffusion \
            assembled by Justin Loroy. \n\n Source Code on [Github](https://github.com/jloroy/shittyidea/blob/main/main.py)")

if input_description:
    chat_prompt_with_values = chat_prompt.format_prompt(description=input_description)
    print(chat_prompt_with_values.to_messages())
    response = chat(chat_prompt_with_values.to_messages()).content
    print(response)
    col1.write(response)

#shitty ideas