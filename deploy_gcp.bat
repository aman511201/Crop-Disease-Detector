@echo off
REM =========================================================================
REM  AgroScan AI - Google Cloud Run 1-Click Deployment Script
REM =========================================================================

echo =============================================================
echo  AgroScan AI - Deploying Crop Disease Detector to Cloud Run
echo =============================================================
echo.

where gcloud >nul 2>nul
if %errorlevel% neq 0 (
    echo [NOTE] Google Cloud SDK (gcloud) is not installed on this PC.
    echo.
    echo EASIEST WAY: Use Google Cloud Shell in your browser (no local installation needed):
    echo 1. Open: https://shell.cloud.google.com
    echo 2. Run:
    echo    git clone https://github.com/aman511201/Crop-Disease-Detector.git
    echo    cd Crop-Disease-Detector
    echo    gcloud run deploy crop-disease-detector --source . --region us-central1 --allow-unauthenticated
    echo.
    pause
    exit /b 1
)

REM Fetch active GCP project
set GCP_PROJECT=
for /f "tokens=*" %%i in ('gcloud config get-value project 2^>nul') do set GCP_PROJECT=%%i

if "%GCP_PROJECT%"=="" (
    set /p GCP_PROJECT="Enter your Google Cloud Project ID: "
)
if "%GCP_PROJECT%"=="(unset)" (
    set /p GCP_PROJECT="Enter your Google Cloud Project ID: "
)

if "%GCP_PROJECT%"=="" (
    echo [ERROR] No Project ID provided. Deployment aborted.
    pause
    exit /b 1
)

echo.
echo Active Project: %GCP_PROJECT%
echo.
echo Step 1: Submitting build to Google Cloud Build...
gcloud builds submit --tag gcr.io/%GCP_PROJECT%/crop-disease-detector

echo.
echo Step 2: Deploying container to Cloud Run...
gcloud run deploy crop-disease-detector ^
    --image gcr.io/%GCP_PROJECT%/crop-disease-detector ^
    --platform managed ^
    --region us-central1 ^
    --allow-unauthenticated ^
    --memory 2Gi ^
    --cpu 2 ^
    --port 8080

echo.
echo [DONE] Deployment complete! Your app is live with HTTPS.
pause
