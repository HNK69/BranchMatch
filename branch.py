import streamlit as st
from branch_recommender import collect_user_preferences, recommend_branch
from career_paths import get_career_paths
from curriculum import load_curriculum
from job_insights import get_salary_data, get_job_growth_data
from job_insights import get_salary_chart_data, get_growth_chart_data
import os
import pandas as pd


from feedback import feedback_form

st.set_page_config(page_title="BranchMatch", layout="wide")
st.title("🎓 BranchMatch - Find Your Ideal Engineering Branch")

st.header("1️⃣ Step 1: Tell us about your interests")
interests = collect_user_preferences()

if st.button("Get My Branch Recommendations"):
    top_branches = recommend_branch(interests)
    st.subheader("🔍 Top Recommended Branches for You:")
    for branch, score in top_branches:
        st.markdown(f"- **{branch}** (score: {score})")

        # Career Paths
        careers = get_career_paths(branch)
        if careers:
            st.markdown(f"  💼 Possible Careers in **{branch}**:")
            for c in careers:
                st.markdown(f"    - {c}")

    st.markdown("---")

    st.header("📚 Step 2: View Branch-wise Curriculum")
    selected_branch = st.selectbox("Select a Branch to View Curriculum", [b for b, _ in top_branches])
    curriculum = load_curriculum(selected_branch)
    for semester, subjects in curriculum:
        with st.expander(f"{semester}"):
            st.write(", ".join(subjects))

    st.markdown("---")

    st.header("📊 Step 3: Job Market Insights")
    salaries = get_salary_data()
    growth = get_job_growth_data()

    st.subheader("💰 Average Salaries (LPA)")
    st.bar_chart(salaries)

    st.subheader("📈 Job Growth Trends")
    for branch in salaries.keys():
        st.markdown(f"- **{branch}**: {growth[branch]} Growth")

    st.markdown("---")

    st.header("🗣️ Step 4: Share Your Thoughts (for Future Students)")
    feedback_form()
import streamlit as st








