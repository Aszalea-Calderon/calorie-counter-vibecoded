import streamlit as st

st.title("Simple Calorie Counter")

if "foods" not in st.session_state:
    st.session_state["foods"] = []
    st.session_state["total_calories"] = 0

food = st.text_input("Food name")
calories = st.number_input("Calories", min_value=0, step=1)

if st.button("Add Food"):
    if food and calories > 0:
        st.session_state["foods"].append((food, calories))
        st.session_state["total_calories"] += calories

# Deduct calories section
st.subheader("Deduct Calories")
deduct_reason = st.text_input("Reason for deduction (e.g., exercise)")
deduct_calories = st.number_input("Calories to deduct", min_value=0, step=1, key="deduct")

if st.button("Deduct"):
    if deduct_reason and deduct_calories > 0:
        st.session_state["foods"].append((f"Deducted: {deduct_reason}", -deduct_calories))
        st.session_state["total_calories"] -= deduct_calories

st.subheader("Foods Added / Calories Adjusted:")
for f, c in st.session_state["foods"]:
    st.write(f"{f}: {c} kcal")

st.subheader(f"Total Calories: {st.session_state['total_calories']} kcal")