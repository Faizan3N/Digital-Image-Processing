DIGITAL IMAGE PROCESSING DEMONSTRATION
# Description:
#   Demonstration of Spatial Filters:
#   - Median, Max, Min (Nonlinear Filters)
#   - Low-pass (Averaging & Gaussian Filters)
#   - High-pass (Laplacian Filter)
#   - High-boost Sharpening
# ---------------------------------------------------------

import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import urllib.request

# ---------------------------------------------------------
# Configure matplotlib for VS Code (TkAgg ensures popup window)
# ---------------------------------------------------------
matplotlib.use('TkAgg')

# ---------------------------------------------------------
# Helper function for image normalization
# ---------------------------------------------------------
def normalize(img):
    """Normalize image values to range 0–255 for correct display"""
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    return img.astype(np.uint8)

# ---------------------------------------------------------
# 1. Download a sample image (Fixed with header)
# ---------------------------------------------------------
url = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response, open("lenna.png", 'wb') as out_file:
        out_file.write(response.read())
    print("✅ Image downloaded successfully!")
    img = cv2.imread("lenna.png", cv2.IMREAD_GRAYSCALE)
except Exception as e:
    print("⚠️ Download failed:", e)
    print("Using fallback: built-in sample image.")
    from skimage import data
    img = data.camera()

# Resize for uniform display
img = cv2.resize(img, (256, 256))

# ---------------------------------------------------------
# 2. Add Salt-and-Pepper Noise (for demonstration)
# ---------------------------------------------------------
noisy_img = img.copy()
prob = 0.03  # 3% of pixels become noisy

# Add salt (white) noise
num_salt = np.ceil(prob * img.size * 0.5)
coords = (np.random.randint(0, img.shape[0], int(num_salt)),
          np.random.randint(0, img.shape[1], int(num_salt)))
noisy_img[coords] = 255

# Add pepper (black) noise
num_pepper = np.ceil(prob * img.size * 0.5)
coords = (np.random.randint(0, img.shape[0], int(num_pepper)),
          np.random.randint(0, img.shape[1], int(num_pepper)))
noisy_img[coords] = 0

# ---------------------------------------------------------
# 3. Apply Nonlinear Filters (Median, Max, Min)
# ---------------------------------------------------------
median_filtered = cv2.medianBlur(noisy_img, 3)
max_filtered = cv2.dilate(noisy_img, np.ones((3, 3), np.uint8))  # Max filter
min_filtered = cv2.erode(noisy_img, np.ones((3, 3), np.uint8))   # Min filter

# ---------------------------------------------------------
# 4. Apply Linear Filters (Low-pass, Gaussian & High-pass)
# ---------------------------------------------------------
# 4.1 Normal Low-pass (Averaging)
low_pass_kernel = np.ones((3, 3), np.float32) / 9
low_pass_filtered = cv2.filter2D(img, -1, low_pass_kernel)
low_pass_filtered = normalize(low_pass_filtered)

# 4.2 Gaussian Low-pass filter (smooths naturally using σ)
# cv2.GaussianBlur(image, kernel_size, sigma)
gaussian_filtered = cv2.GaussianBlur(img, (5, 5), sigmaX=0.8)
#gaussian_filtered = cv2.GaussianBlur(img, (5, 5), sigmaX=1.0)
#gaussian_filtered = cv2.GaussianBlur(img, (5, 5), sigmaX=3.0)
#gaussian_filtered = cv2.GaussianBlur(img, (5, 5), sigmaX=5.0)


gaussian_filtered = normalize(gaussian_filtered)

# 4.3 High-pass (Laplacian)
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])
high_pass_filtered = cv2.filter2D(img, -1, laplacian_kernel)
high_pass_filtered = normalize(high_pass_filtered)

# ---------------------------------------------------------
# 5. High-Boost Sharpening
# ---------------------------------------------------------
alpha = 1.0  # Sharpening strength (try 0.5, 1.0, 1.5)
sharpened = cv2.addWeighted(img, 1, high_pass_filtered, alpha, 0)
sharpened = normalize(sharpened)

# ---------------------------------------------------------
# 6. Display All Results (Fixed layout)
# ---------------------------------------------------------
titles = [
    'Original Image (Lenna)',
    'With Noise (Salt & Pepper)',
    'Median Filtered',
    'Max Filtered',
    'Min Filtered',
    'Low-Pass (Averaging)',
    'Gaussian Low-Pass',
    'High-Pass (Laplacian)',
    'High-Boost Sharpened'
]

images = [
    img, noisy_img, median_filtered, max_filtered,
    min_filtered, low_pass_filtered, gaussian_filtered, high_pass_filtered, sharpened
]

plt.figure(figsize=(15, 12))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.title(titles[i], fontsize=10)
    plt.axis('off')

plt.tight_layout()
plt.show(block=True)

# ---------------------------------------------------------
# 7. Save results as image file
# ---------------------------------------------------------
plt.savefig("filter_results_with_gaussian.png")
print("📸 Results saved as filter_results_with_gaussian.png in current folder.")
