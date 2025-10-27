import streamlit as st

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("Numa - AI Mental Health Assistant")

user_input = st.chat_input("Share your mood or thoughts here...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Simple placeholder chatbot logic:
    response = "Thank you for sharing. I'm here to listen."
    st.session_state["messages"].append({"role": "bot", "content": response})

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])
