def apply_styles(st):
    st.markdown("""
    <style>

    /* ---------- BACKGROUND ---------- */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827, #1e293b);
        background-attachment: fixed;
    }

    body {
        color: #f1f5f9;
        font-family: 'Segoe UI', sans-serif;
    }

    /* ---------- TOP BAR ---------- */
    .top-icons {
        display: flex;
        justify-content: flex-end;
        gap: 15px;
        margin-bottom: 10px;
    }

    .icon-btn {
        background: #1e293b;
        border-radius: 50%;
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        cursor: pointer;
        transition: 0.3s;
        color: #cbd5f5;
    }

    .icon-btn:hover {
        transform: scale(1.1);
        background: #2563eb;
        color: white;
    }

    .profile {
        background: #2563eb;
        color: white;
        font-weight: bold;
    }

    /* ---------- HEADER ---------- */
    .header-card {
        margin-top: -10px;
        margin-bottom: 30px;
    }

    /* ---------- FLASH CARDS ---------- */
    .metric-card {
        background: rgba(30,41,59,0.8);
        padding: 22px;
        border-radius: 14px;
        border-left: 5px solid #2563eb;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        transition: 0.3s;
    }

    .metric-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 30px rgba(37,99,235,0.4);
    }

    /* ---------- CANDIDATE CARD ---------- */
    .candidate-card {
        background: rgba(30,41,59,0.85);
        padding: 25px;
        border-radius: 16px;
        border-left: 6px solid #2563eb;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* ---------- LOGIN BOX ---------- */
    .login-box {
        background: rgba(30,41,59,0.9);
        padding: 40px;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
        max-width: 400px;
        margin: auto;
        margin-top: 80px;
        text-align: center;
        color: #f1f5f9;
    }

    /* ---------- BUTTONS ---------- */
    .stButton>button {
        background: linear-gradient(135deg, #2563eb, #3b82f6);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(37,99,235,0.7);
    }

    .stDownloadButton>button {
        background: linear-gradient(135deg, #1e40af, #2563eb);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }

    </style>
    """, unsafe_allow_html=True)