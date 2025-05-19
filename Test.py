import streamlit as st
from memory_utils import load_memory, save_memory, BASE_GOAL
from food_form import food_form
from deduct_form import deduct_form
from food_list import food_list
from calorie_gauge import calorie_gauge
from design import inject_global_styles

inject_global_styles("dark")

if "foods" not in st.session_state:
    mem = load_memory()
    st.session_state["foods"] = mem.get("foods", [])
    st.session_state["total_eaten"] = mem.get("total_eaten", 0)
    st.session_state["total_burned"] = mem.get("total_burned", 0)
    st.session_state["total_remaining"] = mem.get("total_remaining", BASE_GOAL)

def persist_state():
    foods = st.session_state["foods"]
    total_eaten = sum(c for _, c in foods if c > 0)
    total_burned = -sum(c for _, c in foods if c < 0)
    total_remaining = BASE_GOAL - total_eaten + total_burned
    st.session_state["total_eaten"] = total_eaten
    st.session_state["total_burned"] = total_burned
    st.session_state["total_remaining"] = total_remaining
    save_memory()

st.sidebar.title("Navigation")
if "page" not in st.session_state:
    st.session_state["page"] = "Dashboard"

page = st.sidebar.radio(
    "Go to",
    ("Dashboard", "Calories", "Recipies", "Workouts", "Settings"),
    key="main_nav",
    index=["Dashboard", "Calories", "Recipies", "Workouts", "Settings"].index(st.session_state["page"]) if st.session_state["page"] in ["Dashboard", "Calories", "Recipies", "Workouts", "Settings"] else 0
)

st.session_state["page"] = page

if st.session_state["page"] == "Dashboard":
    st.title("Dashboard")
    st.write("Welcome to your health dashboard!")
elif st.session_state["page"] == "Calories":
    st.title("Simple Calorie Counter")
    col1, col2 = st.columns([2, 1])
    with col1:
        food_form()
        deduct_form()
        st.subheader("Foods Added / Calories Adjusted:")
        food_list()
    with col2:
        calorie_gauge(BASE_GOAL)
    persist_state()
elif st.session_state["page"] == "Recipies":
    st.title("Recipies")
    st.write("Recipe suggestions and tracking coming soon!")
elif st.session_state["page"] == "Workouts":
    st.title("Workouts")
    st.write("Workout logging and suggestions coming soon!")
elif st.session_state["page"] == "Settings":
    st.title("Settings")
    st.write("Settings page coming soon!")
