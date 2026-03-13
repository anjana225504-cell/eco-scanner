import streamlit as st
from openai import OpenAI
import os

# Get API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🌱 AI Eco Product Scanner")

st.write("Enter a product name to analyze its environmental impact.")

product = st.text_input("Enter Product Name")

if st.button("Scan Product"):

    prompt = f"""
    Analyze the environmental sustainability of this product: {product}

    Provide:
    - Material
    - Recyclability
    - Environmental Impact
    - Eco-Friendly Suggestion
    - Eco Score (Low / Medium / High)

    Keep the response short and clear.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    result = response.output_text

    st.subheader("🌍 Sustainability Analysis")
    st.write(result)
