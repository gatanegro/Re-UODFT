# Computing Fractal Self-Similarity of Prime Modular Systems

def fractal_self_similarity(prime_residues, depth=5):
    """Computes a fractal transformation to detect self-similarity in prime residues."""
    S_n = np.array(prime_residues, dtype=np.float64)
    for _ in range(depth):
        S_n = (S_n[:-1] + S_n[1:]) / 2  # Iterative contraction step
        S_n = np.abs(np.sin(S_n * np.pi / 3))  # Introduce periodic transformation
    return S_n

# Apply fractal transformation to mod 5 and mod 7 residues
fractal_mod_5 = fractal_self_similarity(mod_5_residues)
fractal_mod_7 = fractal_self_similarity(mod_7_residues)

# Plot fractal transformation results
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(fractal_mod_5, marker='o', linestyle='-', label="Fractal Scaling (Mod 5)")
plt.title("Fractal Self-Similarity in Mod 5 Prime Residues")
plt.xlabel("Iteration Step")
plt.ylabel("Scaled Value")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(fractal_mod_7, marker='o', linestyle='-', label="Fractal Scaling (Mod 7)")
plt.title("Fractal Self-Similarity in Mod 7 Prime Residues")
plt.xlabel("Iteration Step")
plt.ylabel("Scaled Value")
plt.legend()
plt.grid(True)

plt.show()

# Compute entropy to test fractal randomness
entropy_fractal_mod_5 = entropy(np.bincount(fractal_mod_5.astype(int), minlength=5) / len(fractal_mod_5), base=2)
entropy_fractal_mod_7 = entropy(np.bincount(fractal_mod_7.astype(int), minlength=7) / len(fractal_mod_7), base=2)

# Return entropy measurements for fractal modular distributions
entropy_fractal_mod_5, entropy_fractal_mod_7
Result
(0.0, 0.0)