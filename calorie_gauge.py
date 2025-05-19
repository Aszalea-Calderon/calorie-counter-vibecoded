import streamlit as st
import plotly.graph_objects as go

def calorie_gauge(BASE_GOAL):
    foods = st.session_state["foods"]
    food_total = st.session_state.get("total_eaten", 0)
    exercise_total = st.session_state.get("total_burned", 0)
    calories_remaining = st.session_state.get("total_remaining", BASE_GOAL)
    used = food_total
    exercise = exercise_total

    # Always show all segments, even if zero, to keep color legend
    values = [
        max(0, calories_remaining),
        max(0, used),
        max(0, exercise)
    ]
    # If all values are zero, set at least one to 1 to show the chart
    if sum(values) == 0:
        values = [1, 0, 0]

    # Donut chart for remaining, used, and exercise
    fig = go.Figure(data=[
        go.Pie(
            values=values,
            labels=["Remaining", "Used", "Exercise"],
            hole=0.7,
            marker_colors=["#4285F4", "#e6e6e6", "#FFA500"],
            textinfo='none',
            sort=False,
            direction='clockwise'
        )
    ])
    fig.update_traces(
        hoverinfo='label+value',
        showlegend=False
    )
    fig.update_layout(
        annotations=[
            dict(
                text=f"<b>{calories_remaining:,}</b><br><span style='font-size:18px'>Remaining</span>",
                x=0.5, y=0.5, font_size=32, showarrow=False, align="center"
            )
        ],
        margin=dict(l=10, r=10, t=40, b=10),
        height=300
    )

    st.markdown("### Calories")
    st.markdown("Remaining = Goal - Food + Exercise")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div>🏁 <b>Base Goal</b> <span style='float:right;font-size:22px'>{BASE_GOAL:,}</span></div>
            <div>🍽️ <b>Food</b> <span style='float:right;font-size:22px'>{food_total:,}</span></div>
            <div>🔥 <b>Exercise</b> <span style='float:right;font-size:22px'>{exercise_total:,}</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )
