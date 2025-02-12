# Step 2: Simulating Space-Time as Wave Amplitude (Space) and Frequency (Time)

# Define the structured space-time field function
def structured_space_time(x, t, A=1, k=2*np.pi/10, omega=2*np.pi/5):
    """Models space as wave amplitude and time as wave frequency."""
    return A * np.sin(k * x - omega * t)

# Generate space-time grid
x_vals_sim = np.linspace(0, 10, 100)
t_vals_sim = np.linspace(0, 10, 100)
X_sim, T_sim = np.meshgrid(x_vals_sim, t_vals_sim)
Z_sim = structured_space_time(X_sim, T_sim)

# Plot the structured space-time wave
plt.figure(figsize=(10, 6))
plt.contourf(X_sim, T_sim, Z_sim, cmap="coolwarm", levels=50)
plt.colorbar(label="Wave Amplitude (Space Density)")
plt.title("Collatz-Octave Model: Space-Time as an Emergent Oscillatory Field")
plt.xlabel("Space (Amplitude)")
plt.ylabel("Time (Frequency)")

plt.show()

# Step 3: Simulating Nodes (Matter) as Wave Intersections

# Define a function for energy node formation (wave intersection density)
def energy_nodes(x, t, A_list=[1, 0.8], k_list=[2*np.pi/10, 3*np.pi/10], omega_list=[2*np.pi/5, 4*np.pi/5]):
    """Models energy nodes where multiple waves intersect."""
    return sum(A * np.sin(k * x - omega * t) for A, k, omega in zip(A_list, k_list, omega_list))

# Compute energy node formation
Z_nodes = energy_nodes(X_sim, T_sim)

# Plot wave intersections forming energy nodes
plt.figure(figsize=(10, 6))
plt.contourf(X_sim, T_sim, Z_nodes, cmap="plasma", levels=50)
plt.colorbar(label="Energy Node Density")
plt.title("Collatz-Octave Model: Energy Nodes as Wave Intersections")
plt.xlabel("Space (Amplitude)")
plt.ylabel("Time (Frequency)")
plt.show()