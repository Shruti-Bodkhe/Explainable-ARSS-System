import plotly.io as pio
pio.templates.default = "plotly_dark"
import streamlit as st
import plotly.express as px
import pandas as pd
from collections import Counter

from auth import login, check_auth, logout
from styles import apply_styles
from process import process_resumes

st.set_page_config(layout="wide")
apply_styles(st)

# ---------- LOGIN ----------
if not check_auth():
    login()
    st.stop()

# ---------- TOP RIGHT BAR ----------
col1, col2 = st.columns([10,1])
with col2:
    st.markdown("""
    <div class="top-icons">
        <div class="icon-btn">⎋</div>
        <div class="icon-btn profile">S</div>
    </div>
    """, unsafe_allow_html=True)
    logout()

# ---------- HEADER ----------
st.markdown("""
<div class="header-card">
    <h1>ARSS System</h1>
    <p>AI-powered Resume Screening with Explainable Intelligence</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- SIDEBAR ----------
uploaded_files = st.sidebar.file_uploader("Upload Resumes", accept_multiple_files=True)

job_role = st.sidebar.selectbox("Select Role", [
    "Data Scientist","ML Engineer","Web Developer",
    "Finance Analyst","HR Manager","Marketing Executive"
])

threshold = st.sidebar.slider("Minimum Match %", 0, 100, 40)

run = st.sidebar.button("Run Analysis")

# ---------- MAIN ----------
if run and uploaded_files:

    df = process_resumes(uploaded_files, job_role)

    # ---------- FINAL SCORE ----------
    df["final_score"] = (df["match_percentage"] * 0.6) + (df["bert_match_score"] * 40)

    # ---------- FILTER ----------
    filtered_df = df[df["match_percentage"] >= threshold]

    # ---------- FLASH CARDS ----------
    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"<div class='metric-card'>Top Candidates<br><h2>{len(filtered_df)}</h2></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='metric-card'>Top Match %<br><h2>{df['match_percentage'].max():.1f}</h2></div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='metric-card'>Average Match %<br><h2>{df['match_percentage'].mean():.1f}</h2></div>", unsafe_allow_html=True)

    sel = (df["recommendation"]=="Selected").mean()*100
    col4.markdown(f"<div class='metric-card'>Selection Rate<br><h2>{sel:.1f}%</h2></div>", unsafe_allow_html=True)

    st.write("")

    # ---------- HIRING SUMMARY ----------
    selected = df[df["recommendation"] == "Selected"]
    st.success(f"{len(selected)} candidates recommended out of {len(df)} total resumes")

    # ---------- MODEL INSIGHTS ----------
    st.subheader("Model Insights")

    # Bar chart
    st.plotly_chart(
        px.bar(df, x="resume_file", y="match_percentage", color="recommendation",
               title="Candidate Match Distribution"),
        use_container_width=True
    )

    # Scatter
    st.plotly_chart(
        px.scatter(df, x="match_percentage", y="bert_match_score",
                   title="Semantic vs Skill Alignment",
                   hover_data=["resume_file"]),
        use_container_width=True
    )

    # Pie
    st.plotly_chart(
        px.pie(df, names="recommendation", title="Selection Distribution"),
        use_container_width=True
    )

    st.write("")

    # ---------- SKILL DISTRIBUTION ----------
    st.subheader("Skill Distribution")

    all_skills = sum(df["matched_skills"], [])
    skill_counts = Counter(all_skills)

    skill_df = pd.DataFrame(skill_counts.items(), columns=["Skill", "Count"])

    st.plotly_chart(
        px.bar(skill_df, x="Skill", y="Count", title="Most Common Skills"),
        use_container_width=True
    )

    st.write("")

    # ---------- TOP 5 ----------
    st.subheader("Top 5 Recommended Candidates")
    st.dataframe(df.head(5))

    st.write("")

    # ---------- FILTERED TABLE ----------
    st.subheader("Candidate Ranking (Filtered)")
    st.dataframe(filtered_df)

    st.write("")

    # ---------- TOP CANDIDATE ----------
    top = df.iloc[0]

    st.subheader("Top Candidate")

    st.markdown(f"""
    <div class="candidate-card">
        <h3>{top['resume_file']}</h3>
        <p>Match: {top['match_percentage']:.2f}%</p>
        <p>BERT: {top['bert_match_score']:.3f}</p>
        <p>Final Score: {top['final_score']:.2f}</p>
        <p>Skills: {top['matched_skills']}</p>
        <p>Missing: {top['missing_skills']}</p>
        <p>{top['explanation']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ---------- DOWNLOAD ----------
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "Download Full Report",
        csv,
        "arss_results.csv",
        "text/csv"
    )