<div align="center">

# AGGROWS
### AI-Powered Plant Disease Recognition System

**A smart crop disease detection web app that uses deep learning to identify plant diseases from leaf images.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep_Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Neural_Networks-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![NumPy](https://img.shields.io/badge/NumPy-Image_Processing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

</div>

---

## Overview

**AGGROWS** is an AI-based plant disease recognition system designed to help farmers, students, and researchers detect crop diseases quickly using leaf images. Users can upload an image of a plant leaf, and the trained deep learning model analyzes it to predict whether the plant is healthy or affected by a disease.

The project uses a TensorFlow/Keras model trained on PlantVillage-style crop disease data and provides a simple Streamlit dashboard for image upload, disease prediction, remedies, and prevention product links.

---

## Key Features

- **AI Disease Detection** - Predicts plant diseases from uploaded leaf images.
- **38-Class Classification** - Supports healthy and diseased leaf categories across multiple crops.
- **Streamlit Dashboard** - Simple and interactive web interface.
- **Fast Image Analysis** - Processes uploaded images and returns predictions quickly.
- **Remedy Search Support** - Opens YouTube remedy search results for predicted diseases.
- **Prevention Product Links** - Provides product search links for selected disease categories.
- **Training History Included** - Includes model training metrics for accuracy and validation review.
- **Farmer-Friendly Workflow** - Designed to make crop disease checking easy and accessible.

---

## Model Performance

The included training history shows strong model performance across 10 epochs:

| Metric | Result |
|---|---|
| **Final Training Accuracy** | ~99.07% |
| **Final Validation Accuracy** | ~97.08% |
| **Best Validation Accuracy** | ~97.81% |
| **Total Classes** | 38 |

---

## Supported Crops

AGGROWS supports disease recognition for crops such as:

- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Orange
- Peach
- Bell Pepper
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

The model can detect healthy leaves as well as diseases such as early blight, late blight, black rot, powdery mildew, bacterial spot, rust, leaf mold, mosaic virus, and more.

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python | Core application and model inference |
| **Web App** | Streamlit | Interactive user interface |
| **AI Framework** | TensorFlow / Keras | Deep learning model training and prediction |
| **Image Processing** | NumPy | Image array conversion and preprocessing |
| **Notebook Support** | Jupyter Notebook | Training and testing experiments |
| **Dataset** | PlantVillage-style Dataset | Crop disease image classification |

---

## Project Structure

```text
Aggrows-main/
|-- main.py                                      # Main Streamlit application
|-- test.py                                      # Testing / alternate prediction script
|-- train plant diseases.ipynb                   # Model training notebook
|-- Test Plant Disease Recognition Model(AGGROWS).ipynb
|-- training_hist.json                           # Training and validation metrics
```

---

## Getting Started

### Prerequisites

Before running the project, install:

- Python 3.10 or higher
- pip
- A trained model file named `trained_model.keras`

The Streamlit app expects the trained model file in the project root:

```text
trained_model.keras
```

### Clone the Repository

```bash
git clone https://github.com/your-username/aggrows.git
cd aggrows
```

### Create a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install streamlit tensorflow numpy pillow
```

For notebook usage:

```bash
pip install jupyter matplotlib
```

---

## Run the Application

Start the Streamlit app:

```bash
streamlit run main.py
```

The app will be available at:

```text
http://localhost:8501
```

---

## How It Works

1. Open the AGGROWS dashboard.
2. Navigate to the disease recognition page.
3. Upload a clear image of a plant leaf.
4. Click the analysis button.
5. The AI model predicts the disease class.
6. Use remedy and prevention links for the next steps.

---

## Dataset Information

The project is based on PlantVillage-style image data containing healthy and diseased crop leaves.

| Split | Images |
|---|---:|
| **Training** | 140,591 |
| **Validation** | 35,144 |
| **Testing** | 33 |
| **Classes** | 38 |

---

## Important Notes

- The file `trained_model.keras` is required for predictions.
- Replace any local image paths with relative project assets before publishing.
- Prediction accuracy depends on lighting, image clarity, dataset quality, and model training.
- AGGROWS is a support tool and should not replace expert agricultural advice.

---

## Roadmap

- [ ] Add `requirements.txt`
- [ ] Add confidence score display
- [ ] Add detailed disease remedy database
- [ ] Add more crop and disease classes
- [ ] Add multilingual support for farmers
- [ ] Deploy on Streamlit Community Cloud
- [ ] Replace local image paths with repository assets
- [ ] Add screenshots and demo video

---

## Author

**Aman**  
GitHub: [@CodemasterAman](https://github.com/CodemasterAman)

---

## License

This project can be released under the MIT License. Add a `LICENSE` file to your repository if you want to make it open source.

---

<div align="center">
  <sub>Built to help farmers protect crops with faster and smarter disease detection.</sub>
</div>
