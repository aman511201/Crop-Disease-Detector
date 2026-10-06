#!/usr/bin/env bash
# =========================================================================
#  AgroScan AI - Google Cloud Run 1-Click Deployment Script
# =========================================================================

set -e

echo "============================================================="
echo " AgroScan AI - Deploying Crop Disease Detector to Cloud Run"
echo "============================================================="

if ! command -v gcloud &> /dev/null; then
    echo "[NOTE] gcloud CLI not found."
    echo "Tip: Run this directly in Google Cloud Shell (https://shell.cloud.google.com):"
    echo "  gcloud run deploy crop-disease-detector --source . --region us-central1 --allow-unauthenticated"
    exit 1
fi

GCP_PROJECT=$(gcloud config get-value project 2>/dev/null || true)
if [ -z "$GCP_PROJECT" ] || [ "$GCP_PROJECT" = "(unset)" ]; then
    read -p "Enter your Google Cloud Project ID: " GCP_PROJECT
fi

if [ -z "$GCP_PROJECT" ]; then
    echo "[ERROR] Project ID is required."
    exit 1
fi

echo "Active Project: $GCP_PROJECT"
echo ""
echo "Step 1: Submitting build to Google Cloud Build..."
gcloud builds submit --tag "gcr.io/$GCP_PROJECT/crop-disease-detector"

echo ""
echo "Step 2: Deploying container to Cloud Run..."
gcloud run deploy crop-disease-detector \
    --image "gcr.io/$GCP_PROJECT/crop-disease-detector" \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi \
    --cpu 2 \
    --port 8080

echo ""
echo "[DONE] Deployment complete! Your app is live with HTTPS."
