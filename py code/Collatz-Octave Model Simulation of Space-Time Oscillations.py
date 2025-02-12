# Step 2: Simulating COM’s Effect on Space-Time Structuring

# Define a wave-based space-time structuring function based on COM principles
def com_space_time_wave(x, t, omega=1, k=1):
    """Models a space-time wave oscillation using COM harmonic principles."""
    return np.sin(k * x - omega * t) * np.exp(-0.01 * x)

# Generate space-time grid
x_vals = np.linspace(0, 10, 100)
t_vals = np.linspace(0, 10, 100)
X, T = np.meshgrid(x_vals, t_vals)
Z = com_space_time_wave(X, T)

# Plot the COM-based space-time wave
plt.figure(figsize=(10, 6))
plt.contourf(X, T, Z, cmap="viridis", levels=50)
plt.colorbar(label="Wave Amplitude")
plt.title("Collatz-Octave Model Simulation of Space-Time Oscillations")
plt.xlabel("Space (x)")
plt.ylabel("Time (t)")
plt.show()