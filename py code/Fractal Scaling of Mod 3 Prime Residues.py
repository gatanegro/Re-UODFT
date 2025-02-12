# Compute Fractal Scaling Function for Mod 3 Residues

def fractal_scaling_function(prime_residues, iterations=5):
    """Computes a self-similar fractal transformation on mod 3 prime residues."""
    S_n = np.array(prime_residues, dtype=np.float64)
    for _ in range(iterations):
        S_n = (S_n[:-1] + S_n[1:]) / 2  # Iterative contraction step
        S_n = np.abs(np.sin(S_n * np.pi / 3))  # Introduce periodic transformation
    return S_n

# Apply fractal scaling transformation
scaled_residues = fractal_scaling_function(mod_3_residues)

# Plot the fractal transformation result
plt.figure(figsize=(8, 4))
plt.plot(scaled_residues, marker='o', linestyle='-', label="Fractal Scaling Transformation")
plt.title("Fractal Scaling of Mod 3 Prime Residues")
plt.xlabel("Iteration Step")
plt.ylabel("Scaled Value")
plt.legend()
plt.grid(True)
plt.show()

# Compute Shannon entropy to test randomness of scaled residues
scaled_entropy = entropy(np.bincount(scaled_residues.astype(int), minlength=3) / len(scaled_residues), base=2)

# Return entropy and statistical patterns
scaled_entropy
Result
0.0
