import os
import json
import streamlit as st

BASE_GOAL = 1700
MEMORY_FILE = os.path.join(os.path.dirname(__file__), "memory", "calorie_memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        data = {
            "foods": [],
            "total_eaten": 0,
            "total_burned": 0,
            "total_remaining": BASE_GOAL
        }
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)
        return data
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory():
    data = {
        "foods": st.session_state["foods"],
        "total_eaten": st.session_state.get("total_eaten", 0),
        "total_burned": st.session_state.get("total_burned", 0),
        "total_remaining": st.session_state.get("total_remaining", BASE_GOAL)
    }
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)
