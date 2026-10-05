/**
 * AgroScan AI - Frontend Application Controller
 * Handles drag-drop uploads, live camera capture, AI analysis rendering,
 * visual lesion overlays, text-to-speech, and offline disease handbook.
 */

document.addEventListener("DOMContentLoaded", () => {
    // --- State Variables ---
    let cameraStream = null;
    let currentCameraFacing = "environment"; // default to rear camera on mobile
    let currentDiagnosis = null;
    let isSpeaking = false;
    let speechUtterance = null;
    let encyclopediaData = null;

    // --- DOM Elements ---
    const dropzone = document.getElementById("dropzone");
    const fileInput = document.getElementById("file-input");
    const btnBrowse = document.getElementById("btn-browse");
    const samplesContainer = document.getElementById("samples-container");

    const tabBtns = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    // Camera elements
    const videoStream = document.getElementById("camera-stream");
    const cameraCanvas = document.getElementById("camera-canvas");
    const btnCapture = document.getElementById("btn-capture");
    const btnSwitchCamera = document.getElementById("btn-switch-camera");
    const btnStopCamera = document.getElementById("btn-stop-camera");

    // Sections
    const inputSection = document.getElementById("input-section");
    const loadingSection = document.getElementById("loading-section");
    const errorSection = document.getElementById("error-section");
    const resultsSection = document.getElementById("results-section");

    // Result fields
    const resCropBadge = document.getElementById("res-crop-badge");
    const resDiseaseName = document.getElementById("res-disease-name");
    const resPathogenType = document.getElementById("res-pathogen-type");
    const resScientificName = document.getElementById("res-scientific-name");
    const resSeverityBadge = document.getElementById("res-severity-badge");
    const resConfidence = document.getElementById("res-confidence");
    const circleBar = document.getElementById("circle-bar");

    const metricAffected = document.getElementById("metric-affected");
    const metricSpots = document.getElementById("metric-spots");
    const metricHealth = document.getElementById("metric-health");

    // Image Views
    const viewOriginal = document.getElementById("view-original");
    const viewSegmented = document.getElementById("view-segmented");
    const viewHeatmap = document.getElementById("view-heatmap");
    const viewToggles = document.querySelectorAll(".btn-toggle");

    // Differential Top 3
    const top3Container = document.getElementById("top3-container");

    // Treatments
    const resOrganicList = document.getElementById("res-organic-list");
    const resChemicalList = document.getElementById("res-chemical-list");
    const resPreventionList = document.getElementById("res-prevention-list");
    const resSymptomsText = document.getElementById("res-symptoms-text");
    const resCausesText = document.getElementById("res-causes-text");

    // Action buttons
    const btnScanAnother = document.getElementById("btn-scan-another");
    const btnRetry = document.getElementById("btn-retry");
    const btnReadAloud = document.getElementById("btn-read-aloud");
    const btnPrintReport = document.getElementById("btn-print-report");

    // Modals
    const btnEncyclopedia = document.getElementById("btn-encyclopedia");
    const modalEncyclopedia = document.getElementById("modal-encyclopedia");
    const btnCloseEncyclopedia = document.getElementById("btn-close-encyclopedia");
    const encyclopediaContent = document.getElementById("encyclopedia-content");
    const encyclopediaSearch = document.getElementById("encyclopedia-search");
    const encyclopediaCropFilter = document.getElementById("encyclopedia-crop-filter");

    const btnHistory = document.getElementById("btn-history");
    const modalHistory = document.getElementById("modal-history");
    const btnCloseHistory = document.getElementById("btn-close-history");
    const historyContent = document.getElementById("history-content");
    const btnClearHistory = document.getElementById("btn-clear-history");

    // Theme toggle
    const btnThemeToggle = document.getElementById("btn-theme-toggle");
    const themeIconSun = document.getElementById("theme-icon-sun");
    const themeIconMoon = document.getElementById("theme-icon-moon");

    // =========================================================================
    // Theme Engine
    // =========================================================================
    const savedTheme = localStorage.getItem("agrosan_theme") || "light";
    setTheme(savedTheme);

    btnThemeToggle.addEventListener("click", () => {
        const isDark = document.body.classList.contains("dark-theme");
        setTheme(isDark ? "light" : "dark");
    });

    function setTheme(theme) {
        if (theme === "dark") {
            document.body.classList.add("dark-theme");
            document.body.classList.remove("light-theme");
            themeIconSun.classList.remove("hidden");
            themeIconMoon.classList.add("hidden");
            localStorage.setItem("agrosan_theme", "dark");
        } else {
            document.body.classList.remove("dark-theme");
            document.body.classList.add("light-theme");
            themeIconSun.classList.add("hidden");
            themeIconMoon.classList.remove("hidden");
            localStorage.setItem("agrosan_theme", "light");
        }
    }

    // =========================================================================
    // Tab Navigation & Camera Lifecycle
    // =========================================================================
    tabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const targetTab = btn.getAttribute("data-tab");
            tabBtns.forEach(b => b.classList.remove("active"));
            tabContents.forEach(c => c.classList.remove("active"));

            btn.classList.add("active");
            document.getElementById(targetTab).classList.add("active");

            if (targetTab === "camera-tab") {
                startCamera();
            } else {
                stopCamera();
            }
        });
    });

    // =========================================================================
    // File Upload & Drag & Drop Handling
    // =========================================================================
    btnBrowse.addEventListener("click", () => fileInput.click());
    dropzone.addEventListener("click", (e) => {
        if (e.target !== btnBrowse && !btnBrowse.contains(e.target)) {
            fileInput.click();
        }
    });

    fileInput.addEventListener("change", (e) => {
        if (e.target.files && e.target.files[0]) {
            processSelectedFile(e.target.files[0]);
        }
    });

    ["dragenter", "dragover"].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            dropzone.classList.add("dragover");
        });
    });

    ["dragleave", "drop"].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            dropzone.classList.remove("dragover");
        });
    });

    dropzone.addEventListener("drop", (e) => {
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            processSelectedFile(e.dataTransfer.files[0]);
        }
    });

    function processSelectedFile(file) {
        if (!file.type.startsWith("image/")) {
            showError("Invalid File Format", "Please select a valid image file (JPEG, PNG, WEBP).");
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            const dataUrl = e.target.result;
            // Display preview immediately in original image slot
            viewOriginal.src = dataUrl;
            // Send to backend API
            sendImageForAnalysis({ file: file, previewUrl: dataUrl });
        };
        reader.readAsDataURL(file);
    }

    // =========================================================================
    // Live Camera Stream Handling
    // =========================================================================
    async function startCamera() {
        stopCamera();
        try {
            const constraints = {
                video: {
                    facingMode: { ideal: currentCameraFacing },
                    width: { ideal: 1280 },
                    height: { ideal: 720 }
                }
            };
            cameraStream = await navigator.mediaDevices.getUserMedia(constraints);
            videoStream.srcObject = cameraStream;
        } catch (err) {
            console.error("Camera access error:", err);
            showError("Camera Access Error", "Unable to access device camera. Please check browser camera permissions or upload an image file instead.");
        }
    }

    function stopCamera() {
        if (cameraStream) {
            cameraStream.getTracks().forEach(track => track.stop());
            cameraStream = null;
        }
    }

    btnSwitchCamera.addEventListener("click", () => {
        currentCameraFacing = currentCameraFacing === "user" ? "environment" : "user";
        startCamera();
    });

    btnStopCamera.addEventListener("click", () => {
        stopCamera();
        // Switch back to upload tab
        tabBtns[0].click();
    });

    btnCapture.addEventListener("click", () => {
        if (!videoStream.videoWidth) return;

        cameraCanvas.width = videoStream.videoWidth;
        cameraCanvas.height = videoStream.videoHeight;
        const ctx = cameraCanvas.getContext("2d");
        ctx.drawImage(videoStream, 0, 0, cameraCanvas.width, cameraCanvas.height);

        const dataUrl = cameraCanvas.toDataURL("image/jpeg", 0.92);
        stopCamera();
        viewOriginal.src = dataUrl;
        sendImageForAnalysis({ base64: dataUrl, previewUrl: dataUrl });
    });

    // =========================================================================
    // 1-Click Demo Samples Loader
    // =========================================================================
    async function loadSamples() {
        try {
            const resp = await fetch("/api/samples");
            const data = await resp.json();
            if (data.success && data.samples && data.samples.length > 0) {
                samplesContainer.innerHTML = "";
                data.samples.forEach(sample => {
                    const chip = document.createElement("div");
                    chip.className = "sample-chip";
                    chip.innerHTML = `
                        <img src="${sample.url}" alt="${sample.name}" class="sample-thumb" loading="lazy">
                        <span class="sample-title">${sample.name}</span>
                        <span class="sample-crop">${sample.crop}</span>
                    `;
                    chip.addEventListener("click", () => testSampleImage(sample));
                    samplesContainer.appendChild(chip);
                });
            } else {
                samplesContainer.innerHTML = "<p class='sample-skeleton'>No sample images loaded.</p>";
            }
        } catch (err) {
            console.warn("Could not load samples:", err);
        }
    }

    async function testSampleImage(sample) {
        showLoading("Analyzing " + sample.name + "...");
        try {
            const resp = await fetch(sample.url);
            const blob = await resp.blob();
            const file = new File([blob], sample.filename, { type: "image/jpeg" });
            const dataUrl = sample.url;
            viewOriginal.src = dataUrl;
            sendImageForAnalysis({ file: file, previewUrl: dataUrl });
        } catch (err) {
            showError("Network Error", "Could not fetch sample leaf image.");
        }
    }

    // =========================================================================
    // Backend API Diagnosis Dispatcher
    // =========================================================================
    async function sendImageForAnalysis({ file, base64, previewUrl }) {
        showLoading("Inspecting Leaf Pathology...");

        try {
            let response;
            if (file) {
                const formData = new FormData();
                formData.append("file", file);
                response = await fetch("/api/predict", {
                    method: "POST",
                    body: formData
                });
            } else if (base64) {
                response = await fetch("/api/predict", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ image_data: base64 })
                });
            }

            const data = await response.json();

            if (!data.success) {
                showError(data.error || "Analysis Notice", data.message || "Failed to identify disease.");
                return;
            }

            // Render successful diagnosis
            renderDiagnosisResult(data, previewUrl);

            // Save in history
            saveToHistory(data, previewUrl);

        } catch (err) {
            console.error("Diagnosis request error:", err);
            showError("Server Connection Failed", "Could not connect to AgroScan AI backend. Please verify the Flask server is running.");
        }
    }

    // =========================================================================
    // Diagnosis Result Renderer
    // =========================================================================
    function renderDiagnosisResult(data, previewUrl) {
        currentDiagnosis = data;
        const pred = data.prediction;
        const metrics = data.visual_metrics;

        // Primary Banner
        resCropBadge.textContent = pred.crop;
        resDiseaseName.textContent = pred.disease;
        resPathogenType.textContent = pred.pathogen_type;
        resScientificName.textContent = pred.scientific_name;

        // Severity styling
        if (pred.is_healthy) {
            resSeverityBadge.textContent = "Healthy & Robust";
            resSeverityBadge.className = "meta-tag severity-badge severity-healthy";
        } else {
            resSeverityBadge.textContent = pred.severity + " Severity";
            resSeverityBadge.className = "meta-tag severity-badge";
        }

        // Confidence gauge
        const confVal = pred.confidence;
        resConfidence.textContent = confVal.toFixed(1) + "%";

        // Animate circular gauge
        // Circumference for r=42 is 2 * PI * 42 = 263.89
        const circumference = 263.89;
        const offset = circumference - (confVal / 100) * circumference;
        circleBar.style.strokeDashoffset = offset;
        if (pred.is_healthy) {
            circleBar.style.stroke = "var(--color-primary)";
        } else if (confVal > 85) {
            circleBar.style.stroke = "#ef4444";
        } else {
            circleBar.style.stroke = "#f59e0b";
        }

        // Metrics
        metricAffected.textContent = metrics.affected_percentage.toFixed(1) + "%";
        metricSpots.textContent = metrics.spots_detected + " Spots";
        metricHealth.textContent = metrics.health_score.toFixed(1) + " / 100";

        // Visual Overlays
        viewOriginal.src = previewUrl;
        viewSegmented.src = metrics.annotated_image;
        viewHeatmap.src = metrics.heatmap_image;

        // Reset view toggles to segmented or original
        viewToggles[0].click();

        // Differential Diagnoses (Top 3)
        top3Container.innerHTML = "";
        data.top_3.forEach(item => {
            const itemRow = document.createElement("div");
            itemRow.className = "top3-item";
            itemRow.innerHTML = `
                <div class="top3-name">${item.crop} - ${item.disease}</div>
                <div class="top3-bar-wrap">
                    <div class="top3-bar-fill" style="width: ${item.confidence}%;"></div>
                </div>
                <div class="top3-pct">${item.confidence.toFixed(1)}%</div>
            `;
            top3Container.appendChild(itemRow);
        });

        // Populate Treatment Lists
        populateList(resOrganicList, pred.organic_treatment);
        populateList(resChemicalList, pred.chemical_treatment);
        populateList(resPreventionList, pred.prevention);

        resSymptomsText.textContent = pred.symptoms;
        resCausesText.textContent = pred.causes;

        // Populate Printable Report Data
        document.getElementById("rep-date").textContent = new Date().toLocaleString();
        document.getElementById("rep-crop-disease").textContent = `${pred.crop} — ${pred.disease}`;
        document.getElementById("rep-pathogen").textContent = pred.pathogen_type;
        document.getElementById("rep-scientific").textContent = pred.scientific_name;
        document.getElementById("rep-severity").textContent = pred.severity;
        document.getElementById("rep-conf").textContent = pred.confidence.toFixed(1) + "%";
        document.getElementById("rep-lesion").textContent = metrics.affected_percentage.toFixed(1) + "%";
        document.getElementById("rep-health").textContent = metrics.health_score.toFixed(1) + " / 100";

        populateList(document.getElementById("rep-organic"), pred.organic_treatment);
        populateList(document.getElementById("rep-chemical"), pred.chemical_treatment);
        populateList(document.getElementById("rep-prevention"), pred.prevention);

        // Display results view
        showResults();
    }

    function populateList(ulElement, items) {
        ulElement.innerHTML = "";
        if (items && items.length > 0) {
            items.forEach(txt => {
                const li = document.createElement("li");
                li.textContent = txt;
                ulElement.appendChild(li);
            });
        } else {
            const li = document.createElement("li");
            li.textContent = "No special measures required.";
            ulElement.appendChild(li);
        }
    }

    // =========================================================================
    // Visualizer View Toggles (Original / Lesion / Heatmap)
    // =========================================================================
    viewToggles.forEach(toggle => {
        toggle.addEventListener("click", () => {
            const targetView = toggle.getAttribute("data-view");
            viewToggles.forEach(t => t.classList.remove("active"));
            toggle.classList.add("active");

            viewOriginal.classList.add("hidden");
            viewSegmented.classList.add("hidden");
            viewHeatmap.classList.add("hidden");

            if (targetView === "original") {
                viewOriginal.classList.remove("hidden");
            } else if (targetView === "segmented") {
                viewSegmented.classList.remove("hidden");
            } else if (targetView === "heatmap") {
                viewHeatmap.classList.remove("hidden");
            }
        });
    });

    // =========================================================================
    // UI State Management Helpers
    // =========================================================================
    function showLoading(title) {
        document.getElementById("loader-title").textContent = title || "Inspecting Leaf Tissue...";
        inputSection.classList.add("hidden");
        errorSection.classList.add("hidden");
        resultsSection.classList.add("hidden");
        loadingSection.classList.remove("hidden");
    }

    function showError(title, message) {
        document.getElementById("error-title").textContent = title;
        document.getElementById("error-message").textContent = message;
        loadingSection.classList.add("hidden");
        resultsSection.classList.add("hidden");
        errorSection.classList.remove("hidden");
        inputSection.classList.remove("hidden");
    }

    function showResults() {
        loadingSection.classList.add("hidden");
        errorSection.classList.add("hidden");
        inputSection.classList.add("hidden");
        resultsSection.classList.remove("hidden");
        resultsSection.scrollIntoView({ behavior: "smooth" });
    }

    function resetToUpload() {
        stopSpeech();
        stopCamera();
        fileInput.value = "";
        loadingSection.classList.add("hidden");
        errorSection.classList.add("hidden");
        resultsSection.classList.add("hidden");
        inputSection.classList.remove("hidden");
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    btnScanAnother.addEventListener("click", resetToUpload);
    btnRetry.addEventListener("click", resetToUpload);

    // =========================================================================
    // Text-to-Speech (Voice Reader)
    // =========================================================================
    btnReadAloud.addEventListener("click", () => {
        if (isSpeaking) {
            stopSpeech();
        } else {
            playSpeech();
        }
    });

    function playSpeech() {
        if (!("speechSynthesis" in window) || !currentDiagnosis) {
            alert("Speech synthesis is not supported on this browser.");
            return;
        }

        window.speechSynthesis.cancel();

        const pred = currentDiagnosis.prediction;
        let script = `Diagnosis Report for ${pred.crop}. Identified condition is: ${pred.disease}. `;
        script += `AI Confidence score is ${pred.confidence.toFixed(1)} percent. Severity is ${pred.severity}. `;
        
        if (pred.is_healthy) {
            script += `Your plant is healthy and thriving. Continue routine irrigation and monitoring.`;
        } else {
            script += `Primary organic treatment recommendations are: ${pred.organic_treatment.join(". ")}. `;
            script += `Chemical control options include: ${pred.chemical_treatment.join(". ")}. `;
            script += `To prevent recurrence: ${pred.prevention[0] || "maintain proper spacing and avoid wetting foliage."}`;
        }

        speechUtterance = new SpeechSynthesisUtterance(script);
        speechUtterance.rate = 0.95;
        speechUtterance.pitch = 1.0;

        speechUtterance.onstart = () => {
            isSpeaking = true;
            document.getElementById("read-aloud-text").textContent = "Stop Listening";
            document.getElementById("icon-speaker-play").classList.add("hidden");
            document.getElementById("icon-speaker-stop").classList.remove("hidden");
        };

        speechUtterance.onend = stopSpeech;
        speechUtterance.onerror = stopSpeech;

        window.speechSynthesis.speak(speechUtterance);
    }

    function stopSpeech() {
        if ("speechSynthesis" in window) {
            window.speechSynthesis.cancel();
        }
        isSpeaking = false;
        document.getElementById("read-aloud-text").textContent = "Listen (Read Aloud)";
        document.getElementById("icon-speaker-play").classList.remove("hidden");
        document.getElementById("icon-speaker-stop").classList.add("hidden");
    }

    // =========================================================================
    // Print / PDF Report
    // =========================================================================
    btnPrintReport.addEventListener("click", () => {
        window.print();
    });

    // =========================================================================
    // Disease Encyclopedia Modal
    // =========================================================================
    btnEncyclopedia.addEventListener("click", openEncyclopedia);
    btnCloseEncyclopedia.addEventListener("click", () => modalEncyclopedia.classList.add("hidden"));

    async function openEncyclopedia() {
        modalEncyclopedia.classList.remove("hidden");
        if (!encyclopediaData) {
            encyclopediaContent.innerHTML = "<p>Loading complete disease catalog...</p>";
            try {
                const resp = await fetch("/api/diseases");
                encyclopediaData = await resp.json();
                populateEncyclopediaFilters(encyclopediaData.crops);
                renderEncyclopediaItems(encyclopediaData.crops, "all", "");
            } catch (err) {
                encyclopediaContent.innerHTML = "<p>Failed to load disease library.</p>";
            }
        }
    }

    function populateEncyclopediaFilters(crops) {
        encyclopediaCropFilter.innerHTML = '<option value="all">All Crops</option>';
        Object.keys(crops).sort().forEach(crop => {
            const opt = document.createElement("option");
            opt.value = crop;
            opt.textContent = `${crop} (${crops[crop].length} conditions)`;
            encyclopediaCropFilter.appendChild(opt);
        });
    }

    function renderEncyclopediaItems(crops, selectedCrop, query) {
        encyclopediaContent.innerHTML = "";
        let count = 0;
        const q = query.toLowerCase().trim();

        for (const [cropName, diseaseList] of Object.entries(crops)) {
            if (selectedCrop !== "all" && selectedCrop !== cropName) continue;

            diseaseList.forEach(item => {
                if (q && !item.disease.toLowerCase().includes(q) && !item.symptoms.toLowerCase().includes(q) && !cropName.toLowerCase().includes(q)) {
                    return;
                }
                count++;

                const card = document.createElement("div");
                card.className = "encyclopedia-item";
                card.innerHTML = `
                    <div class="encyclopedia-header">
                        <div>
                            <strong>${item.crop} - ${item.disease}</strong>
                            <span class="meta-tag pathogen-type" style="margin-left: 0.5rem;">${item.pathogen_type}</span>
                        </div>
                        <span>▼</span>
                    </div>
                    <div class="encyclopedia-body hidden">
                        <p><strong>Scientific:</strong> <em>${item.scientific_name}</em> | <strong>Severity:</strong> ${item.severity}</p>
                        <p><strong>Symptoms:</strong> ${item.symptoms}</p>
                        <p><strong>🌿 Organic:</strong> ${item.organic_treatment.join("; ")}</p>
                        <p><strong>🧪 Chemical:</strong> ${item.chemical_treatment.join("; ")}</p>
                        <p><strong>🛡️ Prevention:</strong> ${item.prevention.join("; ")}</p>
                    </div>
                `;

                card.querySelector(".encyclopedia-header").addEventListener("click", () => {
                    const body = card.querySelector(".encyclopedia-body");
                    body.classList.toggle("hidden");
                });

                encyclopediaContent.appendChild(card);
            });
        }

        if (count === 0) {
            encyclopediaContent.innerHTML = "<p style='text-align:center; padding: 2rem;'>No matching crop diseases found.</p>";
        }
    }

    encyclopediaSearch.addEventListener("input", (e) => {
        if (encyclopediaData) {
            renderEncyclopediaItems(encyclopediaData.crops, encyclopediaCropFilter.value, e.target.value);
        }
    });

    encyclopediaCropFilter.addEventListener("change", (e) => {
        if (encyclopediaData) {
            renderEncyclopediaItems(encyclopediaData.crops, e.target.value, encyclopediaSearch.value);
        }
    });

    // =========================================================================
    // History Modal
    // =========================================================================
    btnHistory.addEventListener("click", openHistory);
    btnCloseHistory.addEventListener("click", () => modalHistory.classList.add("hidden"));

    function saveToHistory(result, previewUrl) {
        try {
            const pred = result.prediction;
            const history = JSON.parse(localStorage.getItem("agrosan_history") || "[]");
            const entry = {
                timestamp: new Date().toISOString(),
                crop: pred.crop,
                disease: pred.disease,
                confidence: pred.confidence,
                severity: pred.severity,
                is_healthy: pred.is_healthy,
                thumb: previewUrl
            };
            // Keep last 25 scans
            history.unshift(entry);
            if (history.length > 25) history.pop();
            localStorage.setItem("agrosan_history", JSON.stringify(history));
        } catch (e) {
            console.warn("Storage quota reached for history thumb:", e);
        }
    }

    function openHistory() {
        modalHistory.classList.remove("hidden");
        const history = JSON.parse(localStorage.getItem("agrosan_history") || "[]");
        if (history.length === 0) {
            historyContent.innerHTML = "<div class='history-empty'>No previous leaf scans recorded yet.</div>";
            return;
        }

        historyContent.innerHTML = "";
        history.forEach(item => {
            const dateStr = new Date(item.timestamp).toLocaleString();
            const div = document.createElement("div");
            div.className = "history-item";
            div.innerHTML = `
                <img src="${item.thumb}" class="history-thumb" alt="Thumbnail">
                <div class="history-details">
                    <div class="history-name">${item.crop} - ${item.disease}</div>
                    <div class="history-time">${dateStr} &bull; ${item.confidence.toFixed(1)}% Confidence &bull; ${item.severity}</div>
                </div>
            `;
            historyContent.appendChild(div);
        });
    }

    btnClearHistory.addEventListener("click", () => {
        localStorage.removeItem("agrosan_history");
        historyContent.innerHTML = "<div class='history-empty'>History cleared.</div>";
    });

    // Close modals when clicking backdrop
    [modalEncyclopedia, modalHistory].forEach(modal => {
        modal.querySelector(".modal-backdrop").addEventListener("click", () => {
            modal.classList.add("hidden");
        });
    });

    // =========================================================================
    // Progressive Web App (PWA) & Service Worker Registration
    // =========================================================================
    let deferredPrompt = null;
    const btnInstallApp = document.getElementById("btn-install-app");

    // Capture install prompt
    window.addEventListener("beforeinstallprompt", (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (btnInstallApp) {
            btnInstallApp.classList.remove("hidden");
        }
    });

    if (btnInstallApp) {
        btnInstallApp.addEventListener("click", async () => {
            if (!deferredPrompt) return;
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            if (outcome === "accepted") {
                console.log("User installed AgroScan AI App");
            }
            deferredPrompt = null;
            btnInstallApp.classList.add("hidden");
        });
    }

    window.addEventListener("appinstalled", () => {
        console.log("AgroScan AI was successfully installed as an app!");
        if (btnInstallApp) {
            btnInstallApp.classList.add("hidden");
        }
    });

    // Register Service Worker for offline performance
    if ("serviceWorker" in navigator) {
        window.addEventListener("load", () => {
            navigator.serviceWorker.register("/static/sw.js")
                .then(reg => console.log("AgroScan ServiceWorker registered:", reg.scope))
                .catch(err => console.log("AgroScan ServiceWorker registration failed:", err));
        });
    }

    // Load samples on init
    loadSamples();
});
