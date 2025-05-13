import streamlit as st
def collect_user_preferences():
    interests = {
        "coding": st.slider("Interest in Coding", 0, 10, 5),
        "electronics": st.slider("Interest in Electronics", 0, 10, 5),
        "machines": st.slider("Interest in Working with Machines", 0, 10, 5),
        "design": st.slider("Interest in Designing Structures", 0, 10, 5),
        "math": st.slider("Comfort with Mathematics", 0, 10, 5),
    }
    return interests

def recommend_branch(interests):
    scores = {
        "CSE": interests["coding"] + interests["math"],
        "ECE": interests["electronics"] + interests["math"],
        "Mechanical": interests["machines"],
        "Civil": interests["design"],
        "EEE": interests["electronics"] + interests["machines"],
    }
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]