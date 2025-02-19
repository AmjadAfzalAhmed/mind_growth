import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load Lottie animations
lottie_growth = load_lottieurl("https://lottie.host/4d4b9245-fcd7-4a96-bdc3-4000b174f0e6/Aj3J58V9Fc.json")
lottie_celebration = load_lottieurl("https://lottie.host/269940e6-b38a-4492-a2f8-c4bbc810c7e1/9rPaiGxMx5.json")

# Page configuration
st.set_page_config(page_title="Growth Mindset", page_icon=":kaaba:", layout="wide")



# Load external CSS
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call this function to load the CSS
load_css("style/style.css")


# Title and Introduction
st.title("🌱 What is a Growth Mindset?")
st.write("""
A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes. 
Every challenge is an opportunity to learn and improve.
""")

# Display Lottie animation
if lottie_growth:
    st_lottie(lottie_growth, height=300, key="growth")

# Why Adopt a Growth Mindset?
st.header("Why Adopt a Growth Mindset?")
st.write("""
- **Embrace Challenges**: View obstacles as opportunities to learn rather than as setbacks.
- **Learn from Mistakes**: Understand that making mistakes is a natural part of learning. Each error is a chance to improve.
- **Persist Through Difficulties**: Stay determined, even when things get tough. Hard work and persistence can lead to growth.
- **Celebrate Effort**: Recognize and reward the effort you put into learning, not just the final result.
- **Keep an Open Mind**: Stay curious and be willing to adapt your approach based on what you learn.
""")

# Interactive Chart: Growth Mindset Benefits
st.header("Benefits of a Growth Mindset")
data = {
    "Category": ["Confidence", "Resilience", "Creativity", "Productivity", "Happiness"],
    "Value": [90, 85, 80, 88, 92]
}
df = pd.DataFrame(data)
fig = px.bar(df, x="Category", y="Value", color="Category", title="Impact of a Growth Mindset")
st.plotly_chart(fig, use_container_width=True)

# How Can You Practice a Growth Mindset?
st.header("How Can You Practice a Growth Mindset?")
st.write("""
- **Set Learning Goals**: Instead of only focusing on grades, set goals that help you develop new skills and understand complex concepts.
- **Reflect on Your Learning**: Regularly take time to think about what you’ve learned from both your successes and your challenges.
- **Seek Feedback**: Embrace constructive criticism and use it as a tool for improvement.
- **Stay Positive**: Believe in your capacity to grow, and encourage your peers to do the same.
""")

# Interactive Section: Set Your Goals
st.header("Set Your Growth Goals")
goal = st.text_input("What is one goal you want to achieve?")
if st.button("Add Goal"):
    if goal:
        st.session_state.goals = st.session_state.get("goals", []) + [goal]
        st.success(f"Added goal: {goal}")
    else:
        st.warning("Please enter a goal.")

# Display Goals with Progress Bars
if "goals" in st.session_state:
    st.header("Your Goals")
    for i, goal in enumerate(st.session_state.goals):
        st.markdown(f"<div class='card'><h3>Goal {i+1}: {goal}</h3><div class='progress-bar'><div class='progress-bar-fill' style='width: {min((i+1)*20, 100)}%;'></div></div></div>", unsafe_allow_html=True)

# Celebration Animation
if "goals" in st.session_state and len(st.session_state.goals) >= 5:
    st_lottie(lottie_celebration, height=600, key="celebration")
    st.success("🎉 You're making amazing progress! Keep it up!")

#---Contact information---
with st.container():
    st.write("---")
    st.header("Get in touch wiht me")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/abhutto2006@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" required placeholder="Your name">
        <input type="email" name="email" required placeholder="Your email">
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>    
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# Footer
st.markdown("---")
st.markdown("**Remember**: Your journey in education isn’t just about proving your intelligence—it’s about developing it.♥")