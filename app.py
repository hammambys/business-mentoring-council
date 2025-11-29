import streamlit as st
from council import run_council
import streamlit.components.v1 as components


# Include Google Analytics tracking code
with open("analytics.html", "r") as f:
    html_code = f.read()
    components.html(html_code, height=0)


st.title("🤝 Business Advisor Council")
st.set_page_config(layout="wide")
st.write("Enter your business idea and get advice from our specialists.")

business_idea = st.text_area(
    "💡 Your business idea",
    placeholder="E.g. An AI tool that helps remote teams manage productivity.",
)

colors = {
    "Great opportunity": "green",
    "Needs improvement": "orange",
    "Not worth the risk": "red",
    "Easy": "green",
    "Challenging": "orange",
    "Impossible": "red",
    "Legal": "green",
    "Risky": "orange",
    "Illegal": "red",
}


def extract_sections(text: str) -> dict:
    sections = {}
    current_section = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("Verdict:"):
            current_section = "verdict"
            sections[current_section] = line[len("Verdict:") :].strip()
        elif line.startswith("Reasoning:"):
            current_section = "reasoning"
            sections[current_section] = line[len("Reasoning:") :].strip()
        elif line.startswith("Suggestions:"):
            current_section = "suggestions"
            sections[current_section] = line[len("Suggestions:") :].strip()
        elif current_section:
            sections[current_section] += line + "\n"
    return sections


if st.button("Get Council Advice"):
    if not business_idea.strip():
        st.warning("Please enter a business idea first.")
    else:
        with st.spinner("The Council is discussing your idea..."):
            results = run_council(business_idea)
        st.success("✅ The Council has provided advice!")

        col1, col2, col3 = st.columns(3, gap="medium")

        with col1:
            sections = extract_sections(results["Strategist"])
            verdict_part = sections.get("verdict", "").splitlines()
            reasoning_part = sections.get("reasoning", "").splitlines()
            suggestions_part = sections.get("suggestions", "").splitlines()
            verdict = "".join(verdict_part)
            resoning = "\n".join(reasoning_part)
            suggestions = "\n".join(suggestions_part)

            color = colors.get(verdict.strip(), "black")

            st.subheader("🧠 The Strategist")
            st.write("Feedback from The Strategist:")
            st.write(
                f"<span style='color:{color};font-weight:bold;'>{verdict}</span>",
                unsafe_allow_html=True,
            )
            if reasoning_part:
                st.write("Reasoning:")
                st.write(f"{resoning}")
            if suggestions_part:
                st.write("Suggestions:")
                st.write(f"{suggestions}")

        with col2:
            sections_tech = extract_sections(results["Technologist"])
            verdict_part = sections_tech.get("verdict", "").splitlines()
            reasoning_part = sections_tech.get("reasoning", "").splitlines()
            suggestions_part = sections_tech.get("suggestions", "").splitlines()
            verdict = "".join(verdict_part)
            reasoning = "\n".join(reasoning_part)
            suggestions = "\n".join(suggestions_part)

            color = colors.get(verdict.strip(), "black")

            st.subheader("💻 The Technologist")
            st.write("Feedback from The Technologist:")
            st.write(
                f"<span style='color:{color};font-weight:bold;'>{verdict}</span>",
                unsafe_allow_html=True,
            )
            if reasoning_part:
                st.write("Reasoning:")
                st.write(f"{reasoning}")
            if suggestions_part:
                st.write("Suggestions:")
                st.write(f"{suggestions}")

        with col3:
            sections_tech = extract_sections(results["Lawyer"])
            verdict_part = sections_tech.get("verdict", "").splitlines()
            reasoning_part = sections_tech.get("reasoning", "").splitlines()
            suggestions_part = sections_tech.get("suggestions", "").splitlines()
            verdict = "".join(verdict_part)
            reasoning = "\n".join(reasoning_part)
            suggestions = "\n".join(suggestions_part)

            color = colors.get(verdict.strip(), "black")

            st.subheader("⚖️ The Lawyer")
            st.write("Feedback from The Lawyer:")
            st.write(
                f"<span style='color:{color};font-weight:bold;'>{verdict}</span>",
                unsafe_allow_html=True,
            )
            if reasoning_part:
                st.write("Reasoning:")
                st.write(f"{reasoning}")
            if suggestions_part:
                st.write("Suggestions:")
                st.write(f"{suggestions}")
