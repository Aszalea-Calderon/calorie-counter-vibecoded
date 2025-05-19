import streamlit as st
import json
import os

COMMON_FOODS_PATH = os.path.join(os.path.dirname(__file__), "..", "common_foods.json")

def load_common_foods():
    if not os.path.exists(COMMON_FOODS_PATH):
        with open(COMMON_FOODS_PATH, "w") as f:
            json.dump({}, f)
    with open(COMMON_FOODS_PATH, "r") as f:
        return json.load(f)

def save_common_foods(foods):
    with open(COMMON_FOODS_PATH, "w") as f:
        json.dump(foods, f, indent=2)

if "common_foods" not in st.session_state:
    st.session_state["common_foods"] = load_common_foods()

def food_form():
    if "pending_food" not in st.session_state:
        st.session_state["pending_food"] = ""
    if "pending_calories" not in st.session_state:
        st.session_state["pending_calories"] = 0
    if "pending_quantity" not in st.session_state:
        st.session_state["pending_quantity"] = 1
    if "adding_new_food" not in st.session_state:
        st.session_state["adding_new_food"] = False

    with st.form("add_food_form", clear_on_submit=False):
        food_options = list(st.session_state["common_foods"].keys())
        food_input = st.selectbox(
            "Food name (type to search or add new)",
            options=food_options + ["Add new Food"],
            index=food_options.index(st.session_state["pending_food"]) if st.session_state["pending_food"] in food_options else len(food_options),
            key="food_input"
        )

        # If user types a new food, show "Add new Food"
        if food_input == "Add new Food":
            st.session_state["adding_new_food"] = True
            new_food_name = st.text_input("Enter new food name", value=st.session_state["pending_food"], key="new_food_name")
            calories_per_unit = st.number_input("Calories per unit", min_value=1, step=1, key="new_calories_input")
            quantity = st.number_input("Quantity", min_value=1, step=1, value=st.session_state["pending_quantity"], key="quantity_input")
            total_calories = calories_per_unit * quantity
            st.markdown(f"Total calories: **{total_calories}**")
            add_food = st.form_submit_button("Add Food")
            if add_food and new_food_name and calories_per_unit > 0 and quantity > 0:
                # Add to persistent foods
                st.session_state["common_foods"][new_food_name] = calories_per_unit
                save_common_foods(st.session_state["common_foods"])
                # Add to today's foods
                st.session_state["foods"].append((f"{new_food_name} x{quantity}", total_calories))
                # Reset
                st.session_state["pending_food"] = ""
                st.session_state["pending_calories"] = 0
                st.session_state["pending_quantity"] = 1
                st.session_state["adding_new_food"] = False
        else:
            st.session_state["adding_new_food"] = False
            food = food_input
            calories_per_unit = st.session_state["common_foods"].get(food, 0)
            st.markdown(f"Calories per unit: **{calories_per_unit}**")
            quantity = st.number_input("Quantity", min_value=1, step=1, value=st.session_state["pending_quantity"], key="quantity_input")
            total_calories = calories_per_unit * quantity
            st.markdown(f"Total calories: **{total_calories}**")
            add_food = st.form_submit_button("Add Food")
            if add_food and food and calories_per_unit > 0 and quantity > 0:
                st.session_state["foods"].append((f"{food} x{quantity}", total_calories))
                st.session_state["pending_food"] = ""
                st.session_state["pending_calories"] = 0
                st.session_state["pending_quantity"] = 1
