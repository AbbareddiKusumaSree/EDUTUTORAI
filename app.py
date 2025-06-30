import streamlit as st
from tutor_backend import generate_quiz, evaluate_response

st.title("EduTutor AI")

user_input = st.text_input("Enter your topic or question:")
if user_input:
    quiz = generate_quiz(user_input)
    st.subheader("Generated Quiz:")
    st.write(quiz)
    user_answer = st.text_input("Your answer:")
    if user_answer:
        feedback = evaluate_response(user_input, user_answer)
        st.subheader("Feedback:")
        st.write(feedback)
