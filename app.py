import streamlit as st

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask me anything about college!")

faqs = {
    "admission": "You can apply for admission through the college admission office.",
    "fees": "Please contact the college accounts department for fee details.",
    "courses": "Our college offers BCA, BBA and other courses.",
    "timing": "College timing is 9 AM to 4 PM.",
    "library": "The library is open from 9 AM to 4 PM."
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask your question...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    answer = "Sorry, I don't know the answer."

    for keyword, response in faqs.items():
        if keyword in question.lower():
            answer = response
            break

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()