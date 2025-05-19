import streamlit as st

def inject_global_styles(mode="dark"):
    if mode == "light":
        bg_color = "#ffffff"
        text_color = "#222222"
        input_bg = "#f9f9f9"
        input_border = "#4285F4"
        sidebar_bg = "#f0f2f6"
    else:  # dark
        bg_color = "#18191A"
        text_color = "#f5f6fa"
        input_bg = "#222"
        input_border = "#4285F4"
        sidebar_bg = "#242526"

    st.markdown(
        f"""
        <style>
        html, body, [data-testid="stAppViewContainer"] {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}
        .stApp {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}
        .stTextInput > div > input,
        .stNumberInput > div > input,
        .stTextArea > div > textarea,
        .stSelectbox > div > div {{
            background-color: {input_bg} !important;
            color: {text_color} !important;
        }}
        input:focus, textarea:focus, select:focus {{
            background-color: {input_bg} !important;
            border-color: #fff !important;
            outline: none !important;
        }}
        /* Error state for input fields */
        .stTextInput > div > input[aria-invalid="true"],
        .stNumberInput > div > input[aria-invalid="true"] {{
            background-color: #ffe6e6 !important;
            border-color: #d9534f !important;
        }}
        /* Sidebar background */
        div[data-testid="stSidebar"] {{
            background-color: {sidebar_bg} !important;
            position: relative;
        }}
        /* Profile button at bottom of sidebar */
        .profile-btn {{ position: fixed; bottom: 30px; left: 30px; }}
        </style>
        """,
        unsafe_allow_html=True
    )
