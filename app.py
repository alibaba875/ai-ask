import streamlit as st
from openai import OpenAI
import os

# 1. Ilagay ang iyong OpenAI API Key dito
os.environ["OPENAI_API_KEY"] = "proj-z4HDMUl3RIYJrmBtBbnhsb3e-gBT1VtmfLh-K8pRNuk6TrwaKtnodcTYoJxpdIhh1lw2QA03NwT3BlbkFJQmT4caJ3fP7Whs5ND1wYc9kaKaRHtAjudIZKpMS4u6E2ytJnwlCmpSPee1pWmLyWGGm346UuAA"

st.set_page_config(page_title="Aking Publikong AI", page_icon="🤖")
st.title("🤖 Maligayang Pagdating sa Aking AI!")
st.write("I-type ang iyong tanong sa ibaba upang magsimula.")

# I-initialize ang OpenAI client
client = OpenAI()

# I-initialize ang memory ng chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Isa kang matalino at magalang na AI assistant na sumasagot sa Tagalog o English."}
    ]

# I-display ang mga nakaraang usapan
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Tanggapin ang input ng user
if prompt := st.chat_input("Ano ang maitutulong ko sa iyo ngayon?"):
    # I-display ang mensahe ng user
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Kunin ang tugon mula sa GPT-4o
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state.messages
            )
            full_response = response.choices.message.content
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"❌ Error: {e}"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})