# Solving the Schrödinger Equation for Prime Residue Evolution

from scipy.sparse import diags

# Define parameters for the Schrödinger equation
hbar = 1.0  # Planck's constant (scaled)
mass = 1.0  # Mass (scaled)
N = len(mod_3_residues)
dx = 1.0  # Space step

# Construct discrete Laplacian for kinetic term
diagonal = -2 * np.ones(N)
off_diagonal = np.ones(N - 1)
Laplacian = diags([diagonal, off_diagonal, off_diagonal], [0, -1, 1], format="csr") / (dx**2)

# Define potential function V(x) from mod 3 residues
V = np.array([np.sin(np.pi * res / 3) for res in mod_3_residues])

# Construct Hamiltonian operator H
H_schrodinger = (-hbar**2 / (2 * mass)) * Laplacian + diags(V, 0, format="csr")

# Compute eigenvalues and eigenvectors (Schrödinger states)
eigenvalues_schrodinger, eigenvectors_schrodinger = np.linalg.eigh(H_schrodinger.toarray())

# Plot probability density of first few eigenstates
plt.figure(figsize=(8, 4))
for i in range(5):  # First 5 quantum states
    plt.plot(np.abs(eigenvectors_schrodinger[:, i])**2, label=f"State {i+1}")

plt.title("Probability Densities of Schrödinger States for Prime Residues")
plt.xlabel("Position Index")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()

# Compute mean energy of prime residue quantum states
mean_energy = np.mean(eigenvalues_schrodinger)

# Return mean energy measurement
mean_energy
Result
1.8573651497465944