import streamlit as st
from council import run_council

st.title("🤝 AI Advisor Council (Groq)")
st.write("Enter your business idea and get advice from The Strategist, The Technologist, and The Marketer.")

business_idea = st.text_area("💡 Your business idea", placeholder="E.g. An AI tool that helps remote teams manage productivity.")

if st.button("Get Council Advice"):
    if not business_idea.strip():
        st.warning("Please enter a business idea first.")
    else:
        with st.spinner("The Council is discussing your idea..."):
            results = run_council(business_idea)

        st.success("✅ The Council has provided advice!")

        st.subheader("🧠 Strategist")
        st.write(results["Strategist"])

        st.subheader("💻 Technologist")
        st.write(results["Technologist"])

        st.subheader("📣 Marketer")
        st.write(results["Marketer"])
