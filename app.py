import streamlit as st
from transformers import pipeline

# Load your trained model
qa = pipeline("question-answering", model=model, tokenizer=tokenizer)

st.title("🤖 AI Chatbot")

context = st.text_area("Enter Context", 
"Artificial Intelligence is the simulation of human intelligence processes by machines.")

question = st.text_input("Ask a Question")

if st.button("Get Answer"):
    result = qa(question=question, context=context)
    st.write("Answer:", result["answer"])
    st.write("Confidence:", result["score"])
    import streamlit as st

st.title("🤖 AI Chatbot")

st.write("App is running successfully!")

context = st.text_area("Enter Context")

question = st.text_input("Ask a Question")

if st.button("Get Answer"):
    st.write("You asked:", question)

qa = pipeline("question-answering", model=model, tokenizer=tokenizer)