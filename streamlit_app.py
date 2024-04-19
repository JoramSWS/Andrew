from openai import OpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def page_1():
    PROMPT_TEMPLATE = """
    
    Answer the question in an angry, impatient tone.  Be sarcastic.  Be from Texas.  If you don't know the answer, say "Look, if you crap in one hand and wish in the other, I'll tell you which one fills up first": {question}

    """

    
    # Streamlit App
    htp="https://raw.githubusercontent.com/JoramSWS/pw-tests/main/S1_CrewHero_Wordmark-2x.png"
    st.image(htp, width=350)
    st.title("TVBOY AI")
    st.header("Chris")
    query_text = st.text_input("What??")
    if not query_text:
        st.warning("Please enter your request.")
        return

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(question=query_text)
    print(prompt)

    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        model_kwargs={"top_p": 0.3},
        temperature=0.8
    )

    response_text = model.invoke(prompt)

    # Convert response_text to string
    response_text = str(response_text)

    # Extract text between "content=" and "response_metadata="
    start_index = response_text.find("content=") + len("content=")
    end_index = response_text.find("response_metadata=")
    formatted_response = response_text[start_index:end_index].replace("\\n\\n", "\n").strip()

    st.write(formatted_response)

def page_2():
  # Streamlit App
    htp="https://raw.githubusercontent.com/JoramSWS/pw-tests/main/S1_CrewHero_Wordmark-2x.png"
    st.image(htp, width=350)
    st.title("TVBOY AI")
    st.header("Andrew")
    query_text = st.text_input("Go for Andrew!")
    if not query_text:
        st.warning("Please enter your request.")
        return

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context="I am an angry man", question=query_text)
    print(prompt)

    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        model_kwargs={"top_p": 0.3},
        temperature=0.8
    )

    response_text = model.invoke(prompt)

    # Convert response_text to string
    response_text = str(response_text)

    # Extract text between "content=" and "response_metadata="
    start_index = response_text.find("content=") + len("content=")
    end_index = response_text.find("response_metadata=")
    formatted_response = response_text[start_index:end_index].replace("\\n\\n", "\n").strip()

    st.write(formatted_response)

PAGES = {
    "Chris": page_1,
    "Andrew": page_2
}

def main():
    st.sidebar.title("navigation")
    choice = st.sidebar.selectbox("select chatbot", list(PAGES.keys()))
    #call the page function
    PAGES[choice]()

if __name__ == "__main__":
    main()
