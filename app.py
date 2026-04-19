import streamlit as st
import json
from agents import run_pipeline

st.title("AI Agent-Based Learning System")

# Input
grade = st.number_input("Enter Grade", min_value=1, max_value=10, value=4)
topic = st.text_input("Enter Topic", value="Types of angles")

if st.button("Generate Content"):
    output, review, refined = run_pipeline(grade, topic)

    st.subheader("📘 Generated Content")
    st.json(output)

    st.subheader("🧪 Reviewer Feedback")
    st.json(review)

    if refined:
        st.subheader("🔁 Refined Output")
        st.json(refined)