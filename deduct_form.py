import streamlit as st

def deduct_form():
    with st.form("deduct_calories_form", clear_on_submit=True):
        deduct_reason = st.text_input("Reason for deduction (e.g., exercise)")
        deduct_calories = st.number_input("Calories to deduct", min_value=0, step=1, key="deduct")
        deduct = st.form_submit_button("Deduct")
        if deduct and deduct_reason and deduct_calories > 0:
            st.session_state["foods"].append((f"Deducted: {deduct_reason}", -deduct_calories))
