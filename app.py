import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (AI learns from this)
products = [
    "plastic bottle",
    "plastic bag",
    "glass jar",
    "glass bottle",
    "paper cup",
    "paper bag",
    "steel bottle",
    "metal can"
]

materials = [
    "Plastic",
    "Plastic",
    "Glass",
    "Glass",
    "Paper",
    "Paper",
    "Metal",
    "Metal"
]

# Convert text into numbers for AI
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(products)

# Train AI model
model = MultinomialNB()
model.fit(X, materials)

st.title("🌱 AI Eco Product Scanner")

product = st.text_input("Enter product name")

if st.button("Scan Product"):

    if product == "":
        st.write("Please enter a product")
    else:
        test = vectorizer.transform([product])
        prediction = model.predict(test)[0]

        st.subheader("AI Prediction")

        if prediction == "Plastic":
            st.write("Material:", prediction)
            st.write("Recyclable: Limited")
            st.write("Impact: High pollution risk")
            st.write("Suggestion: Use reusable alternatives")

        elif prediction == "Glass":
            st.write("Material:", prediction)
            st.write("Recyclable: Yes")
            st.write("Impact: Low environmental harm")
            st.write("Suggestion: Reuse glass containers")

        elif prediction == "Paper":
            st.write("Material:", prediction)
            st.write("Recyclable: Yes")
            st.write("Impact: Biodegradable")
            st.write("Suggestion: Use recycled paper")

        elif prediction == "Metal":
            st.write("Material:", prediction)
            st.write("Recyclable: Highly recyclable")
            st.write("Impact: Durable and reusable")
            st.write("Suggestion: Prefer metal containers")
