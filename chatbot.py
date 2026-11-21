

from dotenv import load_dotenv
import streamlit as st
from langchain_ollama import ChatOllama
# from langchain_google_genai import ChatGoogleGenerativeAI

# load the env variable
load_dotenv()


# streamlit page setup
st.set_page_config(
    page_title="💬 Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 GenAi chatbot")

# initialte chat history
if "chat_history" not in st.session_state: 
    st.session_state.chat_history = []

# show chat history on screen
# message = {
    # role: 'user',
    # content: 'Hi'
# }

# Looping through all the chats form chat_history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# llm initiale
llm = ChatOllama(
    model="gemma2:2b",
    temperature=0.1
)

# llm = ChatGoogleGenerativeAI( 
#     model="gemini-4-carbon",
#     temperature=0
# )

# input box
user_prompt = st.chat_input("Ask chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(input=[{"role": "system", "content": "You are a helpful assitant"}, *st.session_state.chat_history])

    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)


# WHOLE FLOW
# -----------

# user query

# display user query (line:45)

# save user query to chat histor

# send chat history to llm

# got response form llm

# save response in chat history

# dipllay llm response(line:54)
        