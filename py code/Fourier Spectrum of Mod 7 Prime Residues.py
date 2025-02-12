# Investigating Modular Prime Systems Beyond Mod 3

# Define function to compute modular residues for different mod bases
def compute_modular_residues(primes, mod_base):
    """Computes modular residues of primes for a given base."""
    return np.array([p % mod_base for p in primes])

# Compute modular residues for mod 5 and mod 7
mod_5_residues = compute_modular_residues(primes, 5)
mod_7_residues = compute_modular_residues(primes, 7)

# Compute Fourier spectra for modular systems
fft_mod_5 = np.abs(fft(mod_5_residues))
fft_mod_7 = np.abs(fft(mod_7_residues))

# Plot Fourier spectra comparisons
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(fft_mod_5, marker='o', linestyle='-', label="Mod 5 Spectrum")
plt.title("Fourier Spectrum of Mod 5 Prime Residues")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(fft_mod_7, marker='o', linestyle='-', label="Mod 7 Spectrum")
plt.title("Fourier Spectrum of Mod 7 Prime Residues")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)

plt.show()

# Compute entropy comparison for modular distributions
entropy_mod_5 = entropy(np.bincount(mod_5_residues, minlength=5) / len(mod_5_residues), base=2)
entropy_mod_7 = entropy(np.bincount(mod_7_residues, minlength=7) / len(mod_7_residues), base=2)

# Return entropy measurements for modular distributions
entropy_mod_5, entropy_mod_7
Result
(2.0599958152682043, 2.6330334105665334)