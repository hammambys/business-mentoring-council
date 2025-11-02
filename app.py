import streamlit as st
from council import run_council

st.title("🤝 AI Advisor Council")
st.set_page_config(layout="wide")
st.write("Enter your business idea and get advice from The Strategist, The Technologist, and The Marketer.")

business_idea = st.text_area("💡 Your business idea", placeholder="E.g. An AI tool that helps remote teams manage productivity.",
                             value="social media app that connects pet owners based on their pets' interests and activities.")


if st.button("Get Council Advice"):
    if not business_idea.strip():
        st.warning("Please enter a business idea first.")
    else:
        with st.spinner("The Council is discussing your idea..."):
            results = run_council(business_idea)
                
        st.success("✅ The Council has provided advice!")

        col1, col2, col3 = st.columns(3)

        with col1:
            verdict_line = ""
            reasoning_line = ""
            for line in results["Strategist"].splitlines():
                if line.lower().startswith("verdict:"):
                    verdict_line = line.split(":", 1)[1].strip()
                elif line.lower().startswith("reasoning:"):
                    reasoning_line = line.split(":", 1)[1].strip()

            # Set color based on verdict
            color = "gray"
            if "great" in verdict_line.lower():
                color = "green"
            elif "improvement" in verdict_line.lower():
                color = "orange"
            elif "risk" in verdict_line.lower():
                color = "red"

            st.subheader("🧠 Strategist")
            st.write(f"<span style='color:{color};font-weight:bold;'>{verdict_line}</span>", unsafe_allow_html=True)
            st.write(f"Reasoning: {reasoning_line}")

        with col2:
            st.subheader("💻 Technologist")
            st.write(results["Technologist"])
        
        with col3:
            st.subheader("📣 Marketer")
            st.write(results["Marketer"])
