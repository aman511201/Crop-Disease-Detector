#!/usr/bin/env bash
# =========================================================================
#  AgroScan AI - Google Cloud Run Deployment Script (Bash / Cloud Shell)
# =========================================================================
set -e

PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [ -z "$PROJECT_ID" ]; then
    echo "Please set your Google Cloud project first:"
    echo "gcloud config set project YOUR_PROJECT_ID"
    exit 1
fi

echo "Deploying AgroScan AI to Google Cloud Project: $PROJECT_ID"

# Enable required Google Cloud services
echo "Enabling Cloud Run, Cloud Build, and Container Registry APIs..."
gcloud services enable run.googleapis.com cloudbuild.googleapis.com containerregistry.googleapis.com

# Build container on Google Cloud
echo "Building container with Cloud Build..."
gcloud builds submit --tag gcr.io/"$PROJECT_ID"/crop-disease-detector

# Deploy to Cloud Run
echo "Deploying to Cloud Run..."
gcloud run deploy crop-disease-detector \
    --image gcr.io/"$PROJECT_ID"/crop-disease-detector \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi \
    --cpu 2 \
    --port 8080

echo "Deployment finished successfully!"
