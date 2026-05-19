import streamlit as st
from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
import chromadb
import os

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# GEMINI SETUP
# ==========================================

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL = "gemini-2.5-flash"

# ==========================================
# CHROMADB SETUP
# ==========================================

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    "rice_knowledge"
)

# ==========================================
# PDF FOLDER
# ==========================================

PDF_FOLDER = "rice_books"

# ==========================================
# LOAD PDF TEXT
# ==========================================

def load_pdfs():

    texts = []

    for file in os.listdir(PDF_FOLDER):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(
                PDF_FOLDER,
                file
            )

            reader = PdfReader(pdf_path)

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    texts.append(text)

    return texts

# ==========================================
# STORE PDF DATA
# ==========================================

def store_pdf_data():

    texts = load_pdfs()

    for i, text in enumerate(texts):

        collection.add(
            documents=[text],
            ids=[str(i)]
        )

# ==========================================
# RETRIEVE CONTEXT
# ==========================================

def retrieve_context(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    documents = results["documents"][0]

    return " ".join(documents)

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Smart Paddy Advisor",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 AI Smart Paddy Farming Advisor")

st.write(
    "Enter your crop details below"
)

# ==========================================
# LOAD PDF KNOWLEDGE
# ==========================================

if st.button("📚 Load Rice PDF Knowledge"):

    store_pdf_data()

    st.success(
        "Rice PDF knowledge loaded successfully!"
    )

# ==========================================
# TEMPERATURE INPUT
# ==========================================

temperature = st.text_input(
    "🌡️ Enter Temperature (°C)"
)

if temperature:

    temp = float(temperature)

    st.subheader("Temperature Advisory")

    if temp < 20:

        st.warning(
            "⚠️ Temperature is low. Rice growth may slow down."
        )

    elif temp <= 35:

        st.success(
            "✅ Temperature is suitable for healthy rice growth."
        )

    else:

        st.error(
            "❌ High temperature may stress the crop and reduce yield."
        )

# ==========================================
# HUMIDITY INPUT
# ==========================================

humidity = st.text_input(
    "💧 Enter Humidity (%)"
)

if humidity:

    hum = float(humidity)

    st.subheader("Humidity Advisory")

    if hum > 85:

        st.warning(
            "⚠️ High humidity may cause fungal diseases."
        )

    elif hum >= 60:

        st.success(
            "✅ Humidity level is good for rice cultivation."
        )

    else:

        st.error(
            "❌ Low humidity may dry the field quickly."
        )

# ==========================================
# SOIL MOISTURE INPUT
# ==========================================

soil = st.text_input(
    "🌱 Enter Soil Moisture (%)"
)

if soil:

    sm = float(soil)

    st.subheader("Soil Moisture Advisory")

    if sm < 30:

        st.error(
            "❌ Soil is dry. Irrigation is needed immediately."
        )

    elif sm <= 70:

        st.success(
            "✅ Soil moisture is optimal for rice growth."
        )

    else:

        st.warning(
            "⚠️ Soil has too much moisture."
        )

# ==========================================
# WATER LEVEL INPUT
# ==========================================

water = st.text_input(
    "🚰 Enter Water Level (cm)"
)

if water:

    wl = float(water)

    st.subheader("Water Level Advisory")

    if wl < 3:

        st.warning(
            "⚠️ Water level is low."
        )

    elif wl <= 6:

        st.success(
            "✅ Water level is ideal."
        )

    else:

        st.error(
            "❌ Excess water detected."
        )

# ==========================================
# PLANT HEIGHT INPUT
# ==========================================

height = st.text_input(
    "📏 Enter Plant Height (cm)"
)

if height:

    ph = float(height)

    st.subheader("Plant Height Advisory")

    if ph < 20:

        st.warning(
            "⚠️ Plant growth is still in early stage."
        )

    elif ph <= 60:

        st.success(
            "✅ Plant growth is healthy."
        )

    else:

        st.success(
            "✅ Rice crop is approaching maturity."
        )

# ==========================================
# CROP AGE INPUT
# ==========================================

age = st.text_input(
    "🌾 Enter Crop Age (days)"
)

growth_stage = ""

if age:

    days = int(age)

    st.subheader("Rice Growth Stage")

    if days <= 15:

        growth_stage = "Germination Stage"

        st.info(
            "🌱 Germination Stage"
        )

    elif days <= 40:

        growth_stage = "Vegetative Stage"

        st.success(
            "🌿 Vegetative Stage"
        )

    elif days <= 60:

        growth_stage = "Tillering Stage"

        st.success(
            "🌾 Tillering Stage"
        )

    elif days <= 90:

        growth_stage = "Reproductive Stage"

        st.success(
            "🌼 Reproductive Stage"
        )

    elif days <= 120:

        growth_stage = "Flowering Stage"

        st.success(
            "🌸 Flowering Stage"
        )

    else:

        growth_stage = "Harvest Stage"

        st.success(
            "🚜 Harvest Stage"
        )

# ==========================================
# FINAL AI ADVISORY
# ==========================================

if (
    temperature and humidity and soil
    and water and height and age
):

    st.divider()

    st.header("🤖 Final AI Advisory")

    if float(soil) < 30:

        st.write(
            "💧 Irrigation is recommended immediately."
        )

    else:

        st.write(
            "✅ Water condition is stable."
        )

    if float(humidity) > 85:

        st.write(
            "⚠️ High humidity may increase fungal disease risk."
        )

    else:

        st.write(
            "✅ Disease risk is currently low."
        )

    if float(temperature) > 35:

        st.write(
            "⚠️ High temperature stress detected."
        )

    else:

        st.write(
            "✅ Temperature is suitable for rice cultivation."
        )

# ==========================================
# ADDITIONAL QUERY SECTION
# ==========================================

st.divider()

st.header("❓ Additional Queries")

farmer_query = st.text_area(
    "Ask any farming question"
)

# ==========================================
# AI RESPONSE
# ==========================================

if st.button("Get AI Answer"):

    if farmer_query:

        context = retrieve_context(
            farmer_query
        )

        prompt = f"""
You are an expert AI Rice Farming Assistant.

Use the rice farming PDF knowledge
to answer the farmer question.

Rice Knowledge:
{context}

Current Field Conditions:

Temperature = {temperature} C
Humidity = {humidity} %
Soil Moisture = {soil} %
Water Level = {water} cm
Plant Height = {height} cm
Crop Age = {age} days
Growth Stage = {growth_stage}

Farmer Question:
{farmer_query}

Give:
1. Simple explanation
2. Proper advisory
3. Disease warning if any
4. Fertilizer suggestion if needed
5. Water management advice

Use simple farmer-friendly language.
"""

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        st.divider()

        st.subheader("🌾 AI Answer")

        st.write(response.text)