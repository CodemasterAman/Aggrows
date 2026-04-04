# AGGROWS: AI-Powered Plant Disease Detection 🌱
import streamlit as st
import tensorflow as tf
import numpy as np
import webbrowser

# ---------- Page Configuration ----------
st.set_page_config(
    page_title="AGGROWS | Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)

# ---------- Custom CSS Styling ----------
st.markdown("""
    <style>
        .stApp {
            background-color: #0e1117;
            color: #e6e6e6;
            font-family: "Segoe UI", sans-serif;
        }
        h1, h2, h3, h4 {
            color: #00ffb7;
            text-align: center;
        }
        .css-18e3th9, .css-1d391kg {
            background-color: #1a1d23;
            border-radius: 10px;
            padding: 20px;
        }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stButton>button {
            background-color: #00b377;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            font-size: 16px;
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #00ffb7;
            color: #000;
            transform: scale(1.05);
        }
        .stSidebar {
            background-color: #1a1d23;
        }
        a {
            color: #00ffb7;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Model Prediction Function ----------
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_model.keras', compile=False)
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions)

# ---------- Disease Classes ----------
class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
              'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
              'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
              'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
              'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
              'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
              'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
              'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
              'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
              'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
              'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
              'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
              'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
              'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

# ---------- Sidebar Navigation ----------
st.sidebar.title("🌿 AGGROWS Dashboard")
app_mode = st.sidebar.radio("Navigate to", ["🏠 Home", "ℹ️ About", "🔍 Disease Recognition"])

# ---------- Home Page ----------
if app_mode == "🏠 Home":
    st.title("🌱 AGGROWS: AI-Based Plant Disease Recognition")
    st.image("C:/Users/amanb/OneDrive/Desktop/pbl dataset/WhatsApp Image 2025-02-22 at 16.33.01_3a8c6b90.jpg", use_container_width=True)
    st.markdown("""
    Welcome to **AGGROWS**, an intelligent system designed to help farmers and researchers identify crop diseases using **AI-based image analysis**.

    ### 🚀 How It Works
    1. **Upload a leaf image** on the Disease Recognition page.  
    2. Our **AI model** analyzes and detects diseases.  
    3. Get **results, remedies, and product links** instantly.

    ### 💡 Why AGGROWS?
    - ⚡ Fast and Accurate Predictions  
    - 🧠 Deep Learning-based Model  
    - 🌍 Mobile Responsive and User-Friendly  
    - 🔗 Instant Remedies & Product Links
    """)

# ---------- About Page ----------
elif app_mode == "ℹ️ About":
    st.title("📘 About AGGROWS")
    st.markdown("""
    **AGGROWS** is an AI-powered platform that detects plant diseases through image recognition.

    #### 🧩 Dataset Information:
    - **Source:** [PlantVillage Dataset](https://github.com/spMohanty/PlantVillage-Dataset)  
    - **Training Images:** 140,591  
    - **Validation Images:** 35,144  
    - **Test Set:** 33  
    - **Total Classes:** 38 (Healthy & Diseased)

    #### ⚙️ Technologies Used:
    - **TensorFlow / Keras** – Model training & inference  
    - **OpenCV & NumPy** – Image processing  
    - **Streamlit** – Interactive web interface  
    - **Python** – Core development language
    """)

# ---------- Disease Recognition Page ----------
elif app_mode == "🔍 Disease Recognition":
    st.title("🌿 AI Disease Recognition")
    test_image = st.file_uploader("📷 Upload a plant leaf image for analysis:")

    if test_image:
        st.image(test_image, caption="Uploaded Image", use_container_width=True)

        if st.button("🔎 Analyze Disease"):
            st.snow()
            result_index = model_prediction(test_image)
            predicted_disease = class_name[result_index]
            st.success(f"🌾 **Detected Disease:** {predicted_disease}")

            # Remedy Search
            if st.button("🎥 Find Remedy on YouTube"):
                search_query = f"{predicted_disease} treatment for plants"
                youtube_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
                webbrowser.open(youtube_url)
                st.markdown(f"[Click here to view remedies on YouTube]({youtube_url})")

            # Product Purchase Links
            product_links = {
                "Apple___Cedar_apple_rust": "https://www.amazon.in/s?k=fungicide+for+apple+cedar+rust",
                "Cherry_(including_sour)___Powdery_mildew": "https://www.amazon.in/s?k=powdery+mildew+fungicide",
            }

            if predicted_disease in product_links:
                if st.button("🛒 Buy Prevention Products"):
                    webbrowser.open(product_links[predicted_disease])
                    st.markdown(f"[Buy on Amazon]({product_links[predicted_disease]})")
