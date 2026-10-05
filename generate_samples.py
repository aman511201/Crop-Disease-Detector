"""
Sample Leaf Generator Script
Generates visually realistic crop leaf images with distinct disease signatures
for quick testing, demos, and evaluation without needing external downloads.
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def create_base_leaf(width=400, height=500, base_color=(50, 160, 45), leaf_type="ovate"):
    """Creates a base organic leaf shape with veins and realistic texture."""
    # Background (neutral field or soft dark desk)
    img = np.full((height, width, 3), (240, 243, 245), dtype=np.uint8)

    # Leaf mask
    mask = np.zeros((height, width), dtype=np.uint8)
    cx, cy = width // 2, height // 2

    if leaf_type == "ovate":
        # Tomato or Potato leaf shape
        pts = []
        for angle in np.linspace(0, 2 * np.pi, 180):
            # Asymmetrical organic leaf curve
            r = 160 * (1 - 0.7 * np.sin(angle)) * (0.95 + 0.05 * np.sin(7 * angle))
            x = int(cx + r * 0.65 * np.cos(angle))
            y = int(cy + 1.2 * r * 0.75 * np.sin(angle) - 20)
            pts.append([x, y])
        cv2.fillPoly(mask, [np.array(pts, dtype=np.int32)], 255)
    elif leaf_type == "elongated":
        # Corn leaf shape
        pts = []
        for angle in np.linspace(0, 2 * np.pi, 180):
            r_x = 75 * (0.95 + 0.05 * np.sin(5 * angle))
            r_y = 210
            x = int(cx + r_x * np.cos(angle))
            y = int(cy + r_y * np.sin(angle))
            pts.append([x, y])
        cv2.fillPoly(mask, [np.array(pts, dtype=np.int32)], 255)
    elif leaf_type == "lobed":
        # Squash / Grape leaf shape
        pts = []
        for angle in np.linspace(0, 2 * np.pi, 240):
            r = 175 * (1 + 0.28 * np.cos(5 * angle) + 0.15 * np.sin(3 * angle))
            x = int(cx + r * 0.9 * np.cos(angle))
            y = int(cy + r * 0.85 * np.sin(angle) - 15)
            pts.append([x, y])
        cv2.fillPoly(mask, [np.array(pts, dtype=np.int32)], 255)
    else:
        # Standard apple / peach oval
        cv2.ellipse(mask, (cx, cy), (120, 190), 0, 0, 360, 255, -1)

    # Smooth mask edges
    mask = cv2.GaussianBlur(mask, (7, 7), 2)
    _, mask_bin = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

    # Base leaf color with organic noise
    noise = np.random.normal(0, 8, (height, width, 3)).astype(np.float32)
    leaf_canvas = np.full((height, width, 3), base_color, dtype=np.float32)
    leaf_canvas = np.clip(leaf_canvas + noise, 0, 255).astype(np.uint8)

    # Draw natural leaf veins
    vein_color = (
        min(255, base_color[0] + 35),
        min(255, base_color[1] + 35),
        min(255, base_color[2] + 25)
    )

    # Central midrib
    cv2.line(leaf_canvas, (cx, cy - 180), (cx, cy + 200), vein_color, 4)

    # Lateral veins
    for y_pos in range(cy - 140, cy + 160, 35):
        # Left vein
        cv2.line(leaf_canvas, (cx, y_pos), (cx - 75, y_pos - 35), vein_color, 2)
        # Right vein
        cv2.line(leaf_canvas, (cx, y_pos + 10), (cx + 75, y_pos - 25), vein_color, 2)

    # Blend leaf onto background using mask
    mask_3d = np.repeat(mask_bin[:, :, np.newaxis], 3, axis=2) / 255.0
    composed = (leaf_canvas * mask_3d + img * (1 - mask_3d)).astype(np.uint8)

    return composed, mask_bin, (cx, cy)


def generate_tomato_early_blight():
    img, mask, (cx, cy) = create_base_leaf(leaf_type="ovate", base_color=(45, 140, 35))

    # Add Early Blight concentric rings ("target spots") with yellow halos
    spots = [
        (cx - 35, cy - 40, 34),
        (cx + 45, cy + 20, 28),
        (cx - 20, cy + 85, 24),
        (cx + 25, cy - 90, 20),
        (cx - 50, cy + 20, 18)
    ]

    for sx, sy, radius in spots:
        # Chlorotic yellow halo
        cv2.circle(img, (sx, sy), int(radius * 1.5), (30, 210, 220), -1)
        # Outer necrotic brown ring
        cv2.circle(img, (sx, sy), radius, (20, 50, 100), -1)
        # Ring 2
        cv2.circle(img, (sx, sy), int(radius * 0.75), (25, 65, 130), 2)
        # Ring 3
        cv2.circle(img, (sx, sy), int(radius * 0.45), (15, 40, 80), -1)
        # Center spot
        cv2.circle(img, (sx, sy), int(radius * 0.2), (10, 25, 50), -1)

    # Re-apply leaf mask to avoid bleed outside
    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def generate_potato_late_blight():
    img, mask, (cx, cy) = create_base_leaf(leaf_type="ovate", base_color=(40, 135, 30))

    # Large irregular water-soaked dark brown / black lesions
    blotches = [
        [(cx - 80, cy - 70), (cx - 10, cy - 50), (cx - 40, cy + 20), (cx - 95, cy - 10)],
        [(cx + 10, cy + 40), (cx + 80, cy + 20), (cx + 90, cy + 100), (cx + 30, cy + 90)],
        [(cx - 20, cy - 140), (cx + 40, cy - 130), (cx + 10, cy - 80), (cx - 30, cy - 100)]
    ]

    for pts in blotches:
        poly = np.array(pts, dtype=np.int32)
        # Pale green water-soaked halo
        cv2.fillPoly(img, [poly], (35, 85, 75))
        # Inner dark necrotic rot
        shrunk = (poly * 0.85 + np.mean(poly, axis=0) * 0.15).astype(np.int32)
        cv2.fillPoly(img, [shrunk], (18, 25, 45))

    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def generate_corn_common_rust():
    img, mask, (cx, cy) = create_base_leaf(leaf_type="elongated", base_color=(50, 155, 40))

    # Cinnamon-brown / golden pustules clustered along corn leaf veins
    np.random.seed(42)
    for _ in range(85):
        rx = int(cx + np.random.normal(0, 28))
        ry = int(cy + np.random.uniform(-160, 160))
        size_x = np.random.randint(3, 7)
        size_y = np.random.randint(6, 14)
        # Rust cinnamon pustule color
        rust_color = (
            int(np.random.randint(15, 35)),
            int(np.random.randint(60, 95)),
            int(np.random.randint(160, 215))
        )
        cv2.ellipse(img, (rx, ry), (size_x, size_y), 0, 0, 360, rust_color, -1)

    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def generate_squash_powdery_mildew():
    img, mask, (cx, cy) = create_base_leaf(leaf_type="lobed", base_color=(45, 145, 40))

    # White powdery fungal coating patches
    powdery_patches = [
        (cx - 50, cy - 30, 48),
        (cx + 40, cy + 25, 42),
        (cx, cy + 80, 36),
        (cx - 30, cy + 50, 30),
        (cx + 60, cy - 60, 35)
    ]

    for px, py, pr in powdery_patches:
        patch = np.zeros_like(img)
        cv2.circle(patch, (px, py), pr, (220, 225, 230), -1)
        patch = cv2.GaussianBlur(patch, (35, 35), 15)
        # Alpha blend powdery patch
        alpha = 0.55
        img = cv2.addWeighted(img, 1.0, patch, alpha, 0)

    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def generate_apple_scab():
    img, mask, (cx, cy) = create_base_leaf(leaf_type="ovate", base_color=(40, 150, 45))

    # Olive-brown velvety lesions with irregular scalloped margins
    lesions = [
        (cx - 30, cy - 60, 28),
        (cx + 35, cy - 20, 24),
        (cx - 25, cy + 40, 26),
        (cx + 20, cy + 70, 22),
        (cx - 45, cy + 10, 18)
    ]

    for lx, ly, lr in lesions:
        pts = []
        for angle in np.linspace(0, 2 * np.pi, 24):
            rad = lr * (0.8 + 0.4 * np.sin(5 * angle))
            x = int(lx + rad * np.cos(angle))
            y = int(ly + rad * np.sin(angle))
            pts.append([x, y])
        cv2.fillPoly(img, [np.array(pts, dtype=np.int32)], (20, 65, 80))

    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def generate_healthy_tomato():
    # Pristine lush green foliage
    img, mask, _ = create_base_leaf(leaf_type="ovate", base_color=(35, 165, 45))
    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def generate_healthy_apple():
    # Crisp, flawless apple foliage
    img, mask, _ = create_base_leaf(leaf_type="standard", base_color=(40, 170, 50))
    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def generate_tomato_yellow_curl():
    img, mask, (cx, cy) = create_base_leaf(leaf_type="ovate", base_color=(60, 180, 80))

    # Pronounced yellowing / chlorosis along margins and cupping
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Brighten and yellow outer areas
    for r in range(height := img.shape[0]):
        for c in range(width := img.shape[1]):
            if mask[r, c] > 0:
                dist = np.hypot(c - cx, r - cy)
                if dist > 80:
                    hsv[r, c, 0] = 26  # Yellow hue
                    hsv[r, c, 1] = min(255, hsv[r, c, 1] + 60)

    img_yellowed = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    bg = np.full_like(img, (240, 243, 245))
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2) / 255.0
    return (img_yellowed * mask_3d + bg * (1 - mask_3d)).astype(np.uint8)


def main():
    target_dir = os.path.join(os.path.dirname(__file__), "static", "samples")
    os.makedirs(target_dir, exist_ok=True)

    samples = {
        "sample_tomato_early_blight.jpg": generate_tomato_early_blight(),
        "sample_potato_late_blight.jpg": generate_potato_late_blight(),
        "sample_corn_common_rust.jpg": generate_corn_common_rust(),
        "sample_squash_powdery_mildew.jpg": generate_squash_powdery_mildew(),
        "sample_apple_scab.jpg": generate_apple_scab(),
        "sample_tomato_healthy.jpg": generate_healthy_tomato(),
        "sample_apple_healthy.jpg": generate_healthy_apple(),
        "sample_tomato_yellow_curl.jpg": generate_tomato_yellow_curl(),
    }

    for fname, mat in samples.items():
        out_path = os.path.join(target_dir, fname)
        cv2.imwrite(out_path, mat)
        print(f"Saved sample: {out_path}")

    print("All sample leaf images created successfully!")


if __name__ == "__main__":
    main()
