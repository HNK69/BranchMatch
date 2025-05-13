import streamlit as st
import pandas as pd
import os

def feedback_form():
    st.header("💬 Feedback")
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        branch = st.selectbox("Branch You Chose", ["CSE", "ECE", "EEE", "Mechanical", "Civil"])
        reason = st.text_area("Why did you choose this branch?")
        submitted = st.form_submit_button("Submit")

        if submitted:
            new_data = pd.DataFrame([[name, branch, reason]], columns=["Name", "Branch", "Reason"])

            if os.path.exists("feedback_data.csv"):
                existing = pd.read_csv("feedback_data.csv")
                updated = pd.concat([existing, new_data], ignore_index=True)
            else:
                updated = new_data

            updated.to_csv("feedback_data.csv", index=False)
            st.success("✅ Thank you for your feedback!")
