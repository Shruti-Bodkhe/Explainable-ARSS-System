import streamlit as st

def login():
    st.markdown("""
    <div class="login-box">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="80"/>
        <h2>ARSS System</h2>
        <p>AI Resume Screening Platform</p>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state["auth"] = True
        else:
            st.error("Invalid credentials")

def check_auth():
    return st.session_state.get("auth", False)

def logout():
    if st.button("Logout"):
        st.session_state["auth"] = False