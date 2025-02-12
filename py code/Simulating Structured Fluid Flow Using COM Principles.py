# Step 1: Simulating Structured Fluid Flow Using COM Principles

# Define the Navier-Stokes velocity field with COM structuring
def structured_fluid_velocity(x, t, A=1, k=2*np.pi/10, omega=2*np.pi/5, viscosity=0.01):
    """Models fluid velocity as a structured oscillatory flow based on COM principles."""
    return A * np.sin(k * x - omega * t) * np.exp(-viscosity * x)

# Generate spatial and temporal grid for fluid simulation
x_vals_fluid = np.linspace(0, 20, 100)
t_vals_fluid = np.linspace(0, 20, 100)
X_fluid, T_fluid = np.meshgrid(x_vals_fluid, t_vals_fluid)
Z_fluid = structured_fluid_velocity(X_fluid, T_fluid)

# Plot the structured fluid velocity field
plt.figure(figsize=(10, 6))
plt.contourf(X_fluid, T_fluid, Z_fluid, cmap="coolwarm", levels=50)
plt.colorbar(label="Fluid Velocity (Structured Flow)")
plt.title("Collatz-Octave Model: Structured Fluid Flow in Navier-Stokes System")
plt.xlabel("Space (Wave Amplitude)")
plt.ylabel("Time (Wave Frequency)")
plt.show()

# Step 2: Computing Gradient to Identify Turbulence Formation

# Compute velocity gradients to check for turbulence formation
velocity_gradient_x = np.gradient(Z_fluid, axis=0)  # Spatial gradient
velocity_gradient_t = np.gradient(Z_fluid, axis=1)  # Temporal gradient

# Compute total turbulence intensity (gradient magnitude)
turbulence_intensity = np.sqrt(velocity_gradient_x**2 + velocity_gradient_t**2)

# Plot turbulence intensity map
plt.figure(figsize=(10, 6))
plt.contourf(X_fluid, T_fluid, turbulence_intensity, cmap="inferno", levels=50)
plt.colorbar(label="Turbulence Intensity (Velocity Gradient Magnitude)")
plt.title("Collatz-Octave Model: Detecting Turbulence in Navier-Stokes Flow")
plt.xlabel("Space (Wave Amplitude)")
plt.ylabel("Time (Wave Frequency)")
plt.show()