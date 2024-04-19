from openai import OpenAI
import streamlit as st


# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def page_1():
    st.title("Chris")
"""
My name is Chris. 
I know many things, ask me anything you like, 
but please. Don't ask me stupid questions❓
"""


if prompt := st.text_input("Ask me anything..."):
    messages = [
        {"role": "system", "content": "You are a sarcastic assistant called Cercei Lannister, you love to use emojis."},
        {"role": "user", "content": prompt}
    ]

    st.chat_message("user").write(prompt)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=messages)
    msg = response.choices[0].message

    st.chat_message("assistant").write(msg.content)

def page_2():
    st.title("Andrew")
"""
My name is Andres. 
I know many things, ask me anything you like, 
but please. Don't ask me stupid questions❓
"""

openai.api_key = openai_api_key

if prompt := st.text_input("Ask me anything..."):
    messages = [
        {"role": "system", "content": "You are very kind and complimentary"},
        {"role": "user", "content": prompt}
    ]

    st.chat_message("user").write(prompt)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=messages)
    msg = response.choices[0].message

    st.chat_message("assistant").write(msg.content)



def main():
    st.sidebar.title("navigation")
    choice = st.sidebar.selectbox("select chatbot", list(PAGES.keys()))
    #call the page function
    PAGES[choice]()

if __name__ == "__main__":
    main()
