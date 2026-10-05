@echo off
REM =========================================================================
REM  AgroScan AI - Google Cloud Run 1-Click Deployment Script
REM =========================================================================

echo -------------------------------------------------------------
echo  AgroScan AI - Deploying Crop Disease Detector to Google Cloud Run
echo -------------------------------------------------------------

where gcloud >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Google Cloud SDK (gcloud) is not found in PATH.
    echo Please install it from: https://cloud.google.com/sdk/docs/install
    echo Or use Google Cloud Shell in your browser (no installation needed!).
    pause
    exit /b 1
)

echo.
echo Step 1: Submitting build to Google Cloud Build...
gcloud builds submit --tag gcr.io/PROJECT_ID/crop-disease-detector

echo.
echo Step 2: Deploying container to Cloud Run...
gcloud run deploy crop-disease-detector ^
    --image gcr.io/PROJECT_ID/crop-disease-detector ^
    --platform managed ^
    --region us-central1 ^
    --allow-unauthenticated ^
    --memory 2Gi ^
    --cpu 2 ^
    --port 8080

echo.
echo [DONE] Deployment complete! Your app is live with HTTPS.
pause
