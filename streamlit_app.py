from openai import OpenAI
import streamlit as st

st.title("ChatGPT-like clone")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
openai_model = "gpt-3.5-turbo"

name = st.radio(
    "Select a name:",
    ["Chris", "Andrew"],
)

personality_prompt = {
    "Chris": "Gruff tone with a fondness for wordplay and portmanteaus,",
    "Andrew": "From Texas, boisterous, angry tone,",
}[name]

if prompt := st.text_input("What is up?"):
    with st.beta_container():
        st.markdown("User:")
        st.write(prompt)

    with st.beta_container():
        st.markdown("Assistant:")
        messages = [{"role": "user", "content": prompt}, {"role": "assistant", "content": personality_prompt}]
        response = client.chat.completions.create(
            model=openai_model,
            messages=messages,
        )
        st.write(response["choices"][0]["message"]["content"].strip())
