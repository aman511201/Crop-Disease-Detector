"""
Leaf Visualizer and Lesion Segmentation Module
Uses OpenCV to segment leaf contours, isolate diseased lesions (chlorosis/necrosis),
estimate severity percentage, and produce visual diagnostic heatmaps.
"""

import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image


class LeafVisualizer:
    def __init__(self):
        pass

    @staticmethod
    def is_plant_leaf(image_bgr: np.ndarray) -> tuple[bool, float, str]:
        """
        Validates whether the uploaded photo actually depicts a plant leaf.
        Checks for typical leaf color profiles (greens, yellow-greens, browns)
        and texture variance.
        """
        hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        # Mask for green vegetation
        green_mask = cv2.inRange(hsv, (25, 40, 30), (88, 255, 255))
        # Mask for yellow/chlorotic leaf tissue
        yellow_mask = cv2.inRange(hsv, (12, 50, 40), (25, 255, 255))
        # Mask for necrotic/brown diseased leaf tissue
        brown_mask = cv2.inRange(hsv, (5, 30, 20), (20, 200, 200))

        leaf_tissue_mask = green_mask | yellow_mask | brown_mask
        leaf_pixel_ratio = np.count_nonzero(leaf_tissue_mask) / (image_bgr.shape[0] * image_bgr.shape[1])

        # Also check color variance to avoid flat solid green backgrounds
        std_dev = np.std(image_bgr)

        if leaf_pixel_ratio < 0.05:
            return False, float(leaf_pixel_ratio), "Insufficient leaf or plant foliage detected in image."
        if std_dev < 12.0:
            return False, float(leaf_pixel_ratio), "Image appears blank or lacks plant structure."

        return True, float(leaf_pixel_ratio), "Valid plant leaf detected."

    @staticmethod
    def analyze_and_overlay(image_bgr: np.ndarray) -> dict:
        """
        Extracts leaf mask, detects necrotic/chlorotic diseased spots,
        computes affected percentage, and creates visual overlays:
        1. Annotated lesion overlay (bounding boxes + glowing contours)
        2. Attention/Disease Heatmap
        3. Segmented leaf on clean background
        """
        h, w = image_bgr.shape[:2]
        # Standardize max dimension for consistent visual processing
        target_size = 640
        scale = target_size / max(h, w)
        if scale < 1.0:
            img = cv2.resize(image_bgr, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
        else:
            img = image_bgr.copy()

        ih, iw = img.shape[:2]

        # 1. Segment entire leaf from background
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        blur = cv2.GaussianBlur(img, (5, 5), 0)

        # Plant foliage HSV ranges (healthy green + diseased shades)
        plant_mask = cv2.inRange(hsv, (15, 30, 25), (95, 255, 255))
        # Include darker necrotic foliage
        dark_necrosis_mask = cv2.inRange(hsv, (0, 30, 20), (20, 220, 180))
        # Include powdery white patches if high contrast
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, otsu_mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        combined_leaf = plant_mask | dark_necrosis_mask
        kernel_leaf = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        combined_leaf = cv2.morphologyEx(combined_leaf, cv2.MORPH_CLOSE, kernel_leaf, iterations=2)
        combined_leaf = cv2.morphologyEx(combined_leaf, cv2.MORPH_OPEN, kernel_leaf, iterations=1)

        # Find largest leaf contour to discard background noise
        contours, _ = cv2.findContours(combined_leaf, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        leaf_mask = np.zeros((ih, iw), dtype=np.uint8)
        if contours:
            # Keep contours with reasonable area (> 5% of image)
            valid_contours = [c for c in contours if cv2.contourArea(c) > (ih * iw * 0.03)]
            if valid_contours:
                cv2.drawContours(leaf_mask, valid_contours, -1, 255, -1)
            else:
                leaf_mask = combined_leaf
        else:
            leaf_mask = combined_leaf

        total_leaf_pixels = np.count_nonzero(leaf_mask)
        if total_leaf_pixels == 0:
            total_leaf_pixels = ih * iw
            leaf_mask[:, :] = 255

        # 2. Isolate diseased / lesion areas within the leaf
        # Diseased areas typically show low Green-to-Red ratio, elevated A/B in LAB, or specific HSV hue shifts
        # Chlorosis (yellowing)
        chlorosis_mask = cv2.inRange(hsv, (15, 60, 60), (32, 255, 255))
        # Necrosis (brown, black, rust spots)
        necrosis_mask = cv2.inRange(hsv, (0, 40, 20), (16, 255, 200))
        # High value white mold / powdery mildew (low saturation + high lightness/value)
        h_chan, s_chan, v_chan = cv2.split(hsv)
        l_channel, a_channel, b_channel = cv2.split(lab)
        powdery_mask = ((s_chan < 125) & (v_chan > 150) & (l_channel > 140)) & leaf_mask

        lesion_mask_raw = (chlorosis_mask | necrosis_mask | powdery_mask) & leaf_mask

        # Clean noise
        kernel_lesion = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        lesion_mask = cv2.morphologyEx(lesion_mask_raw, cv2.MORPH_OPEN, kernel_lesion, iterations=1)
        lesion_mask = cv2.morphologyEx(lesion_mask, cv2.MORPH_CLOSE, kernel_lesion, iterations=1)

        diseased_pixels = np.count_nonzero(lesion_mask)
        affected_percentage = round(float((diseased_pixels / total_leaf_pixels) * 100), 1)

        # Cap between 0% and 100%
        affected_percentage = min(100.0, max(0.0, affected_percentage))

        # 3. Create Annotated Lesion Overlay
        annotated_overlay = img.copy()
        lesion_contours, _ = cv2.findContours(lesion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Highlight diseased clusters
        spots_detected = 0
        for cnt in lesion_contours:
            area = cv2.contourArea(cnt)
            if area > 18:
                spots_detected += 1
                # Draw subtle perimeter in bright coral/red
                cv2.drawContours(annotated_overlay, [cnt], -1, (0, 50, 240), 2)
                # For significant spots, add a bounding box
                if area > 120:
                    bx, by, bw, bh = cv2.boundingRect(cnt)
                    cv2.rectangle(annotated_overlay, (bx, by), (bx + bw, by + bh), (40, 160, 255), 1)

        # Add translucent colored mask for lesions
        color_mask = np.zeros_like(img)
        color_mask[lesion_mask > 0] = [30, 70, 255]  # Vibrant reddish-orange in BGR
        annotated_overlay = cv2.addWeighted(annotated_overlay, 0.82, color_mask, 0.45, 0)

        # Outline the leaf boundary in neon green
        leaf_contours, _ = cv2.findContours(leaf_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(annotated_overlay, leaf_contours, -1, (80, 230, 80), 2)

        # 4. Generate Diagnostic Heatmap (Attention Colormap)
        # Apply distance transform and Gaussian blur to create smooth density heatmap
        density = cv2.GaussianBlur(lesion_mask.astype(np.float32), (31, 31), 11)
        if density.max() > 0:
            density_norm = (density / density.max() * 255).astype(np.uint8)
        else:
            density_norm = np.zeros((ih, iw), dtype=np.uint8)

        heatmap_bgr = cv2.applyColorMap(density_norm, cv2.COLORMAP_JET)
        # Mask heatmap strictly to leaf area
        heatmap_masked = np.zeros_like(img)
        heatmap_masked[leaf_mask > 0] = heatmap_bgr[leaf_mask > 0]

        # Blend heatmap with original image
        blended_heatmap = cv2.addWeighted(img, 0.60, heatmap_masked, 0.40, 0)

        # Encode images to base64 for direct browser rendering
        def to_base64_jpeg(image_mat):
            _, buf = cv2.imencode(".jpg", image_mat, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            return "data:image/jpeg;base64," + base64.b64encode(buf).decode("utf-8")

        return {
            "affected_percentage": affected_percentage,
            "spots_detected": spots_detected,
            "has_significant_lesions": affected_percentage > 2.5,
            "annotated_image": to_base64_jpeg(annotated_overlay),
            "heatmap_image": to_base64_jpeg(blended_heatmap),
            "leaf_mask": leaf_mask
        }
