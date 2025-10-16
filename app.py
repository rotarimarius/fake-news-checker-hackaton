import streamlit as st

# --- Page title ---
st.title("📰 Political News Checker")
st.write(
    "This app helps you quickly check whether a news article might be misleading or false."
)

# --- Input from user ---
st.subheader("Paste your news article or headline here:")
news_text = st.text_area("Enter text here:", height=150)

# --- Fake-news detection simulation ---
# (For demo purposes, this randomly classifies the text)
import random

if st.button("Check News"):
    if not news_text.strip():
        st.warning("Please enter some text first!")
    else:
        # Simulate a check
        result = random.choice(["Likely True ✅", "Possibly False ⚠️", "Needs Verification ❗"])
        st.markdown(f"### Result: {result}")
        st.info(
            "Note: This is a demo. For real-world applications, integrate a proper fact-checking API."
        )

# --- Optional tips section ---
st.subheader("Tips to spot fake news:")
st.markdown("""
- Check the source: Is it reputable?
- Look for supporting evidence and references.
- Watch out for emotionally charged headlines.
- Cross-check with other reliable news outlets.
""")
