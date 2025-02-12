# Step 7: Applying Spectral Analysis and Entropy Scaling to Refine Turbulence Validation

from scipy.fft import fft2, fftshift

# Compute 2D Fourier Transform of experimental turbulence data
turbulence_exp_spectrum = np.abs(fftshift(fft2(turbulence_experimental)))

# Compute 2D Fourier Transform of COM high Reynolds turbulence prediction
turbulence_com_spectrum = np.abs(fftshift(fft2(Z_high_reynolds)))

# Compute entropy of turbulence distributions to analyze complexity and order
def compute_entropy(data):
    """Computes Shannon entropy of a turbulence dataset."""
    hist, bin_edges = np.histogram(data.flatten(), bins=100, density=True)
    hist = hist[hist > 0]  # Remove zero values to avoid log issues
    return -np.sum(hist * np.log2(hist))

entropy_exp = compute_entropy(turbulence_experimental)
entropy_com = compute_entropy(Z_high_reynolds)

# Plot spectral analysis comparison
plt.figure(figsize=(12, 6))

# Plot experimental turbulence spectrum
plt.subplot(1, 2, 1)
plt.imshow(np.log1p(turbulence_exp_spectrum), cmap="plasma", aspect="auto")
plt.colorbar(label="Log-Spectral Intensity")
plt.title("Spectral Analysis: Experimental Turbulence (Fourier Space)")
plt.xlabel("Spatial Frequency")
plt.ylabel("Temporal Frequency")

# Plot COM predicted turbulence spectrum
plt.subplot(1, 2, 2)
plt.imshow(np.log1p(turbulence_com_spectrum), cmap="inferno", aspect="auto")
plt.colorbar(label="Log-Spectral Intensity")
plt.title("Spectral Analysis: COM Predicted Turbulence (Fourier Space)")
plt.xlabel("Spatial Frequency")
plt.ylabel("Temporal Frequency")

plt.tight_layout()
plt.show()

# Return entropy comparison results
entropy_exp, entropy_com
Result
(33.68600951967606, 24.581535671633986)