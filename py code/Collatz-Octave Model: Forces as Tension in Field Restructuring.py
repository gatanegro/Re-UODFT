# Step 4: Simulating Force Scaling as a Function of Wave Amplitude

# Define force as the gradient of the space-time wave function
def force_scaling(x, t, A=1, k=2*np.pi/10, omega=2*np.pi/5):
    """Models forces as field tension gradients in wave structuring."""
    return -np.gradient(structured_space_time(x, t, A, k, omega), x, axis=0)

# Compute force scaling from wave gradients
force_values = force_scaling(X_sim, T_sim)

# Plot force scaling as a function of space-time structuring
plt.figure(figsize=(10, 6))
plt.contourf(X_sim, T_sim, force_values, cmap="inferno", levels=50)
plt.colorbar(label="Force Magnitude (Field Tension Gradient)")
plt.title("Collatz-Octave Model: Forces as Tension in Field Restructuring")
plt.xlabel("Space (Amplitude)")
plt.ylabel("Time (Frequency)")
plt.show()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[53], line 9
      6     return -np.gradient(structured_space_time(x, t, A, k, omega), x, axis=0)
      8 # Compute force scaling from wave gradients
----> 9 force_values = force_scaling(X_sim, T_sim)
     11 # Plot force scaling as a function of space-time structuring
     12 plt.figure(figsize=(10, 6))

Cell In[53], line 6, in force_scaling(x, t, A, k, omega)
      4 def force_scaling(x, t, A=1, k=2*np.pi/10, omega=2*np.pi/5):
      5     """Models forces as field tension gradients in wave structuring."""
----> 6     return -np.gradient(structured_space_time(x, t, A, k, omega), x, axis=0)

File <__array_function__ internals>:200, in gradient(*args, **kwargs)

File ~/.local/lib/python3.11/site-packages/numpy/lib/function_base.py:1169, in gradient(f, axis, edge_order, *varargs)
   1167     continue
   1168 elif distances.ndim != 1:
-> 1169     raise ValueError("distances must be either scalars or 1d")
   1170 if len(distances) != f.shape[axes[i]]:
   1171     raise ValueError("when 1d, distances must match "
   1172                      "the length of the corresponding dimension")

ValueError: distances must be either scalars or 1

# Step 4 (Fixed): Simulating Force Scaling as a Function of Wave Amplitude

# Compute the space-time structured wave
wave_field = structured_space_time(X_sim, T_sim)

# Compute the spatial gradient (force field tension scaling)
force_values_x = np.gradient(wave_field, axis=0)  # Gradient along space (x)
force_values_t = np.gradient(wave_field, axis=1)  # Gradient along time (t)

# Compute total force as combined tension gradient
force_magnitude = np.sqrt(force_values_x**2 + force_values_t**2)

# Plot force scaling as a function of space-time structuring
plt.figure(figsize=(10, 6))
plt.contourf(X_sim, T_sim, force_magnitude, cmap="inferno", levels=50)
plt.colorbar(label="Force Magnitude (Field Tension Gradient)")
plt.title("Collatz-Octave Model: Forces as Tension in Field Restructuring")
plt.xlabel("Space (Amplitude)")
plt.ylabel("Time (Frequency)")
plt.show()