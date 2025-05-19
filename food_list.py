import streamlit as st

def food_list():
    for f, c in st.session_state["foods"]:
        st.write(f"{f}: {c} kcal")
