# Compute Prime Residue Attractor Function

def prime_residue_attractor(prime_residues, iterations=10):
    """Computes an attractor function for mod 3 prime residues."""
    A_n = np.array(prime_residues, dtype=np.float64)
    for _ in range(iterations):
        A_n = np.cumsum(A_n) / np.arange(1, len(A_n) + 1)  # Running average
        A_n = np.abs(np.sin(A_n * np.pi / 3))  # Nonlinear contraction
    return A_n

# Apply attractor function transformation
attractor_residues = prime_residue_attractor(mod_3_residues)

# Plot attractor stabilization
plt.figure(figsize=(8, 4))
plt.plot(attractor_residues, marker='o', linestyle='-', label="Prime Residue Attractor")
plt.title("Prime Residue Attractor Convergence")
plt.xlabel("Iteration Step")
plt.ylabel("Attractor Value")
plt.legend()
plt.grid(True)
plt.show()

# Check variance to see if the attractor stabilizes
attractor_variance = np.var(attractor_residues)

# Return variance measurement to test attractor stability
attractor_variance
Result
1.793033017483448e-08