import streamlit as st
from agents import get_strategist_advice

st.title("🧠 AI Strategist Agent (using Groq)")
st.write("Enter your business idea and get advice from The Strategist.")

business_idea = st.text_area("💡 Your business idea", placeholder="E.g. An AI app that helps freelancers manage clients more efficiently.")

if st.button("Get Advice"):
    if not business_idea.strip():
        st.warning("Please enter a business idea first.")
    else:
        with st.spinner("🧠 Thinking..."):
            advice = get_strategist_advice(business_idea)
        st.success("✅ Advice received!")
        st.subheader("Strategist's Advice")
        st.write(advice)
