import streamlit as st
from textblob import TextBlob

# Title
st.title("😊 AI Sentiment Analyzer")

# User input
text = st.text_area(
    "Enter your text here"
)

# Analyze button
if st.button("Analyze"):

    # Check if input is empty
    if text.strip() == "":
        st.warning("Please enter some text")

    else:

        # Analyze sentiment
        analysis = TextBlob(text)

        polarity = analysis.sentiment.polarity

        # Show polarity score
        st.write("Polarity Score:", round(polarity, 2))

        # Sentiment result
        if polarity > 0:

            st.success("Positive 😊")

        elif polarity < 0:

            st.error("Negative 😞")

        else:

            st.info("Neutral 😐")