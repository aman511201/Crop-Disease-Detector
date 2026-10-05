"""
AgroScan AI - Crop Disease Detection Application
Flask Backend Server providing API endpoints for leaf disease diagnosis,
lesion segmentation, disease encyclopedia, and sample image testing.
"""

import os
import io
import base64
import logging
from flask import Flask, render_template, request, jsonify, send_from_directory
from PIL import Image
import numpy as np

from model.classifier import CropDiseaseClassifier
from model.disease_data import DISEASE_CLASSES, DISEASE_DETAILS, get_disease_info

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024  # 25 MB max upload

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgroScan")

# Initialize AI Classifier
logger.info("Initializing Crop Disease AI Classifier...")
classifier = CropDiseaseClassifier()
logger.info("Crop Disease AI Classifier ready.")


@app.route("/")
def index():
    """Serves the main application page."""
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def predict():
    """
    Accepts an uploaded leaf photo (multipart file or base64 data URL),
    runs the PyTorch MobileNetV2 + OpenCV visualizer pipeline,
    and returns comprehensive disease diagnosis and treatment advice.
    """
    try:
        image_pil = None

        # Check for direct multipart file upload
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != "":
                image_bytes = file.read()
                image_pil = Image.open(io.BytesIO(image_bytes))

        # Check for JSON base64 image (from live camera capture)
        elif request.is_json:
            data = request.get_json()
            if "image_data" in data:
                b64_str = data["image_data"]
                # Strip header if present (e.g. data:image/jpeg;base64,...)
                if "," in b64_str:
                    b64_str = b64_str.split(",", 1)[1]
                image_bytes = base64.b64decode(b64_str)
                image_pil = Image.open(io.BytesIO(image_bytes))

        if image_pil is None:
            return jsonify({
                "success": False,
                "error": "No image provided",
                "message": "Please select a leaf image file or capture a photo using your camera."
            }), 400

        # Ensure RGB format
        image_pil = image_pil.convert("RGB")

        # Run diagnosis pipeline
        result = classifier.predict(image_pil)
        return jsonify(result)

    except Exception as e:
        logger.error(f"Error during diagnosis: {str(e)}", exc_info=True)
        return jsonify({
            "success": False,
            "error": "Processing error",
            "message": f"Could not process image: {str(e)}"
        }), 500


@app.route("/api/diseases", methods=["GET"])
def get_diseases():
    """Returns the complete 38-class crop disease knowledge base."""
    # Organize by crop for convenient browsing in the frontend
    crops = {}
    for key, info in DISEASE_DETAILS.items():
        crop_name = info["crop"]
        if crop_name not in crops:
            crops[crop_name] = []
        entry = info.copy()
        entry["class_key"] = key
        crops[crop_name].append(entry)

    return jsonify({
        "success": True,
        "total_classes": len(DISEASE_CLASSES),
        "crops": crops,
        "classes": DISEASE_CLASSES
    })


@app.route("/api/samples", methods=["GET"])
def get_samples():
    """Returns the list of available demo sample leaf images."""
    sample_dir = os.path.join(app.static_folder, "samples")
    samples = []
    if os.path.exists(sample_dir):
        meta_lookup = {
            "sample_tomato_early_blight.jpg": {
                "name": "Tomato Early Blight",
                "crop": "Tomato",
                "desc": "Concentric rings & target spots"
            },
            "sample_corn_common_rust.jpg": {
                "name": "Corn Common Rust",
                "crop": "Corn (Maize)",
                "desc": "Cinnamon-brown pustules"
            },
            "sample_squash_powdery_mildew.jpg": {
                "name": "Squash Powdery Mildew",
                "crop": "Squash",
                "desc": "White powdery fungal coating"
            },
            "sample_potato_late_blight.jpg": {
                "name": "Potato Late Blight",
                "crop": "Potato",
                "desc": "Dark water-soaked necrotic rot"
            },
            "sample_apple_scab.jpg": {
                "name": "Apple Scab",
                "crop": "Apple",
                "desc": "Olive-brown velvety lesions"
            },
            "sample_tomato_yellow_curl.jpg": {
                "name": "Tomato Yellow Leaf Curl",
                "crop": "Tomato",
                "desc": "Severe chlorosis & margin curling"
            },
            "sample_tomato_healthy.jpg": {
                "name": "Healthy Tomato Leaf",
                "crop": "Tomato",
                "desc": "Unblemished green foliage"
            },
            "sample_apple_healthy.jpg": {
                "name": "Healthy Apple Leaf",
                "crop": "Apple",
                "desc": "Clean crisp leaf lamina"
            }
        }

        for fname in sorted(os.listdir(sample_dir)):
            if fname.lower().endswith((".jpg", ".jpeg", ".png")):
                info = meta_lookup.get(fname, {
                    "name": fname.replace("sample_", "").replace(".jpg", "").replace("_", " ").title(),
                    "crop": "General",
                    "desc": "Crop leaf sample"
                })
                samples.append({
                    "filename": fname,
                    "url": f"/static/samples/{fname}",
                    "name": info["name"],
                    "crop": info["crop"],
                    "desc": info["desc"]
                })

    return jsonify({
        "success": True,
        "samples": samples
    })


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "app": "AgroScan AI - Crop Disease Detection",
        "device": str(classifier.device),
        "total_classes": classifier.num_classes
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
