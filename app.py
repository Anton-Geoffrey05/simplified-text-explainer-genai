import streamlit as st
from prompt_templates import simplify_prompt
from gemini_engine import generate_simplified_text

st.set_page_config(page_title="Text Explainer", layout="centered")

st.title("📘 Simplified Legal / Medical Text Explainer (Gemini)")

domain = st.selectbox("Select Domain", ["Legal", "Medical"])
input_text = st.text_area("Paste complex text here", height=250)

if st.button("Simplify"):
    if input_text.strip() == "":
        st.warning("Please enter text")
    else:
        prompt = simplify_prompt(input_text, domain)
        output = generate_simplified_text(prompt)
        st.subheader("🔍 Simplified Output")
        st.write(output)

