# AgroScan AI - Crop Disease Detection & Plant Doctor 🌿🔬

> An AI-powered agricultural diagnostic application for instant crop leaf disease detection, physical lesion segmentation, confidence rating, organic & chemical treatments, and long-term prevention advice.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/aman511201/Crop-Disease-Detector)

---

## 🌟 Key Features

1. **Dual Input Modes**:
   - **📁 High-Res Image Upload**: Drag-and-drop or browse JPG, PNG, WEBP, or AVIF files.
   - **📷 Live Camera Viewfinder**: Capture leaves directly in the field using your smartphone or desktop webcam with front/rear camera toggle.
   - **⚡ 1-Click Demo Samples**: Preloaded sample test cards (Tomato Early Blight, Potato Late Blight, Corn Rust, Squash Powdery Mildew, Apple Scab, etc.) for instant evaluation.

2. **Deep Learning Classification Engine**:
   - Built on **PyTorch MobileNetV2** optimized for edge and CPU inference.
   - Covers **38 standard PlantVillage categories** across **14 major agricultural crops**:
     - *Tomato, Potato, Corn (Maize), Apple, Grape, Bell Pepper, Cherry, Peach, Strawberry, Squash, Orange (Citrus), Blueberry, Raspberry, Soybean*.
   - Rejects non-leaf images with informative feedback.

3. **OpenCV Lesion Segmentation & Diagnostic Overlays**:
   - **Original Leaf View**: High-resolution input capture.
   - **Lesion Contour Overlay**: Highlights active necrotic and chlorotic tissue with glowing perimeters and bounding boxes.
   - **Thermal Attention Heatmap**: Diagnostic colormap illustrating high-density pathogen clusters.
   - **Leaf Metrics**: Calculates Affected Surface Area (%), Diseased Spots Count, and overall Plant Health Score (0-100).

4. **Actionable Agricultural Prescriptions**:
   - 🌿 **Organic & Biological Control**: Neem oil, *Bacillus subtilis*, *Trichoderma*, copper soaps, selective pruning.
   - 🧪 **Chemical Fungicides & Pesticides**: Specific active ingredients (Chlorothalonil, Mancozeb, Azoxystrobin, etc.) and application guidance.
   - 🛡️ **Long-Term Cultural Prevention**: Drip irrigation, crop rotation, seed sanitation, canopy aeration.
   - 🔍 **Causal Agent & Weather Drivers**: Pathogen classification (Fungus / Bacteria / Virus / Pest / Oomycete) and favorable humidity/temperature ranges.

5. **Farmer Field Utility Tools**:
   - 🔊 **Voice Reader (Text-to-Speech)**: Speaks out diagnosis and spray recommendations aloud for field workers.
   - 📄 **One-Click Printable / PDF Report**: Formatted phytosanitary diagnosis report sheet ready for printing or archiving.
   - 📖 **Disease Encyclopedia**: Built-in searchable handbook of all 38 conditions with symptoms and cures.
   - 🕒 **Scan History**: Stores recent scans in local storage for side-by-side comparison.

---

## 📁 Project Architecture

```
crop-disease-detector/
├── app.py                     # Flask web server and REST API endpoints
├── requirements.txt           # Python dependency specifications
├── train_or_export.py         # PyTorch MobileNetV2 trainer & weight exporter
├── generate_samples.py        # Realistic synthetic sample leaf generator
├── test_classifier.py         # Verification and test suite for AI pipeline
├── model/
│   ├── classifier.py          # PyTorch inference pipeline & symptom logit fusion
│   ├── disease_data.py        # 38-class agricultural disease knowledge base
│   ├── visualizer.py          # OpenCV leaf segmentation, lesion masks & heatmaps
│   └── weights/
│       └── crop_disease_model.pth # Exported calibrated PyTorch weights
├── static/
│   ├── css/
│   │   └── style.css          # AgriTech responsive design & dark mode
│   ├── js/
│   │   └── main.js            # Camera handling, drag-drop, TTS & UI controls
│   └── samples/               # Sample leaf images for 1-click testing
└── templates/
    └── index.html             # Web application interface
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.10, 3.11, 3.12, 3.13, and 3.14)
- Pip package manager

### 2. Installation

Clone or open the project folder in your terminal:
```bash
cd "computer vision"
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Launch the Flask development server:
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 📡 REST API Endpoints

### 1. `POST /api/predict`
Uploads a leaf image and returns the disease diagnosis, top 3 differentials, and visual overlay images.

- **Request**: Multipart Form Data (`file: <binary image>`) OR JSON (`{"image_data": "<base64>"}`)
- **Response**:
```json
{
  "success": true,
  "leaf_detected": true,
  "prediction": {
    "crop": "Tomato",
    "disease": "Early Blight",
    "scientific_name": "Alternaria solani",
    "pathogen_type": "Fungus",
    "confidence": 98.8,
    "severity": "Moderate to High",
    "is_healthy": false,
    "symptoms": "Dark brown to black spots with concentric rings...",
    "causes": "Warm temperatures (24°C–29°C), high humidity...",
    "organic_treatment": [
      "Prune off affected lower leaves...",
      "Apply copper fungicide or potassium bicarbonate..."
    ],
    "chemical_treatment": [
      "Chlorothalonil, Mancozeb, Azoxystrobin, or Pyraclostrobin."
    ],
    "prevention": [
      "Space tomato plants 24-36 inches apart...",
      "Practice 3-year crop rotation..."
    ]
  },
  "visual_metrics": {
    "affected_percentage": 14.2,
    "spots_detected": 6,
    "health_score": 68.4,
    "annotated_image": "data:image/jpeg;base64,...",
    "heatmap_image": "data:image/jpeg;base64,..."
  },
  "top_3": [
    { "crop": "Tomato", "disease": "Early Blight", "confidence": 98.8 },
    { "crop": "Potato", "disease": "Early Blight", "confidence": 1.1 },
    { "crop": "Tomato", "disease": "Target Spot", "confidence": 0.1 }
  ]
}
```

### 2. `GET /api/diseases`
Retrieves all 38 diseases grouped by crop with full symptoms and treatments.

### 3. `GET /api/samples`
Returns available demo sample images for quick testing.

### 4. `GET /api/health`
Health check endpoint reporting device status (CPU/CUDA) and model readiness.

---

## 🏋️‍♂️ Custom Dataset Training & Weight Export

To train the classification head on your own custom dataset (e.g. downloaded PlantVillage dataset arranged in standard `ImageFolder` subdirectories):

```bash
python train_or_export.py --data_dir /path/to/dataset --epochs 10 --batch_size 32 --lr 0.001
```

Weights will automatically save to [model/weights/crop_disease_model.pth](file:///C:/Users/amanp/OneDrive/Desktop/computer%20vision/model/weights/crop_disease_model.pth) and be loaded automatically by `app.py`.

---

## 🧪 Running Automated Tests

Run the test suite to verify model inference, lesion segmentation, and sample diagnoses:
```bash
python test_classifier.py
```

---

## ☁️ Deployment Guide

### Option 1: 1-Click Free Deployment on Render (Recommended)
1. Click the badge: [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/aman511201/Crop-Disease-Detector)
2. Sign in with GitHub on [Render](https://render.com).
3. Click **Apply / Create Web Service**. Render builds the Docker container automatically and gives you a free live URL (e.g. `https://crop-disease-detector.onrender.com`).

### Option 2: Google Cloud Run via Cloud Shell (No local installation needed)
If you don't have `gcloud` installed locally:
1. Open [Google Cloud Shell](https://shell.cloud.google.com).
2. Clone and deploy directly:
   ```bash
   git clone https://github.com/aman511201/Crop-Disease-Detector.git
   cd Crop-Disease-Detector
   gcloud run deploy crop-disease-detector \
       --source . \
       --region us-central1 \
       --allow-unauthenticated \
       --memory 2Gi \
       --cpu 2
   ```
3. Cloud Shell will output your live HTTPS URL.

### Option 3: Hugging Face Spaces (Free CPU Docker Space)
1. Go to [huggingface.co/new-space](https://huggingface.co/new-space).
2. Choose **Docker** as Space SDK.
3. Push or connect this repository.
