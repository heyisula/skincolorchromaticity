# Skin Color Detection Using Chromaticity

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Statistical%20Model-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-11557C?style=for-the-badge&logo=python&logoColor=white)

![Status](https://img.shields.io/badge/Status-Complete-2ea44f?style=for-the-badge)

---

## Overview

This project implements a **statistical skin colour detection system** using chromaticity space. The model learns the distribution of skin pixel colours from a labelled dataset and uses **Mahalanobis distance** to classify each pixel in a new image as either skin or non-skin.

The key idea is that converting raw RGB values to **chromaticity coordinates** removes the effect of lighting, making skin detection more consistent across different conditions.

---

## How It Works

Raw RGB values change with lighting — the same skin under bright or dim light gives very different R, G, B numbers. Chromaticity normalises this by dividing each channel by the total intensity:

```
x = R / (R + G + B)
y = G / (R + G + B)
```

Skin pixels form a **tight cluster** in this 2D chromaticity space regardless of brightness. We model that cluster with a **Gaussian distribution** (mean + covariance), then classify any new pixel by measuring how far it sits from that cluster.

---

## Dataset

![Dataset](https://img.shields.io/badge/Dataset-Pratheepan%20Skin%20Dataset-brightgreen?style=flat-square)
![Images](https://img.shields.io/badge/Images-32%20Face%20Photos-blue?style=flat-square)
![Ground Truth](https://img.shields.io/badge/Ground%20Truth-Included-success?style=flat-square)

**Pratheepan Skin Dataset** — [cs-chan.com](http://cs-chan.com/downloads_skin_dataset.html)

Images collected from Google covering a range of skin tones, lighting conditions, and backgrounds. Each image comes with a ground truth mask where white pixels indicate actual skin regions.

---

## Folder Structure

```
project/
│
├── data/
│   ├── images/           # Full original photos
│   ├── skin_cropped/     # Manually cropped skin regions (used for training)
│   └── ground_truth/     # Binary masks (white = skin, black = non-skin)
│
├── out/                  # All output images saved here
│
├── skin_detection.ipynb  # Main notebook
└── README.md
```

> Make sure the `out/` folder exists before running, or create it with `os.makedirs('out', exist_ok=True)`.

---

## Notebook Walkthrough

| Cell | Description |
|------|-------------|
| **1** | Import libraries — `cv2`, `numpy`, `matplotlib`, `os` |
| **2** | Set dataset folder paths |
| **3** | Load and count image files |
| **4** | Visualise sample images alongside their cropped skin regions |
| **5** | Visualise chromaticity x and y channels on sample images |
| **6** | Extract skin pixel chromaticity values from cropped skin images |
| **7** | Build the skin model — compute **mean** and **covariance matrix** |
| **8** | Collect non-skin pixel samples from full images |
| **9** | Build the non-skin model for comparison |
| **10** | Plot skin vs non-skin pixel distributions in chromaticity space |
| **11** | `skin_detection()` function + threshold comparison across values 2, 5, 10, 15, 20 |
| **12** | `evaluateSkinNonSkinDetection()` — full visual output with ground truth comparison |

---

## Detection Pipeline

```
Input Image
     │
     ▼
Convert to Chromaticity (x, y)
     │
     ▼
Compute Mahalanobis Distance from Skin Mean
     │
     ▼
Apply Threshold  ──────────────────────────┐
     │                                     │
  distance < threshold             distance >= threshold
     │                                     │
  SKIN (1)                            NON-SKIN (0)
```

---

## Output

For each image the notebook produces a 5-column visual:

| Column | Description |
|--------|-------------|
| Original Image | The unmodified input photo |
| Binary Mask | White = detected skin, Black = non-skin |
| Skin Only | Original colours kept only where skin is detected |
| Skin + Grey BG | Skin in real colour, non-skin converted to greyscale |
| Ground Truth | The correct answer mask from the dataset |

All outputs are saved to the `out/` folder as `.png` files.

---

## Key Functions

```python
# Convert RGB image to chromaticity coordinates
convert_to_chromaticity(img)
    → returns x, y  (arrays of same shape as image)

# Detect skin pixels using Mahalanobis distance
skin_detection(image, meanValue, conInverse, Threshold)
    → returns binary mask  (1 = skin, 0 = non-skin)

# Produce skin-only and combined visualisation
evaluateSkinNonSkinDetection(image, mask)
    → returns skinOnly, combinedImg
```

---

## Requirements

```bash
pip install opencv-python numpy matplotlib
```

| Library | Version | Purpose |
|---------|---------|---------|
| `opencv-python` | 4.x | Image loading, colour conversion |
| `numpy` | any | Matrix operations, statistics |
| `matplotlib` | any | Plotting and visualisation |

---

## Running the Notebook

```bash
# Clone or download the project folder
# Place the Pratheepan dataset into data/ as shown above
# Launch Jupyter
jupyter notebook skin_detection.ipynb
# Run all cells top to bottom
```

---

## Results Saved

| File | Description |
|------|-------------|
| `out/sample_images_cropped_and_original.png` | Dataset sample preview |
| `out/chromaticity_conversion_samples.png` | Chromaticity x/y visualisation |
| `out/skin_chromaticity_distribution.png` | Skin pixel cluster plot |
| `out/skin_non_skin_chromaticity_distribution.png` | Skin vs non-skin scatter plot |
| `out/skin_detection_result.png` | Final 5-column detection output |

---

## References

> W.R. Tan, C.S. Chan, Y. Pratheepan and J. Condell — *A Fusion Approach for Efficient Human Skin Detection*, IEEE Transactions on Industrial Informatics, vol.8(1):138-147, 2012.
