# Step 6: Computing the Minimum Energy Gap (E_gap) When Waves Intersect to Form a Node/Particle

# Define a function to compute the energy gap based on COM harmonic node formation
def com_energy_gap(n, alpha=1/137):
    """Computes the minimum energy required to form a stable energy node (particle)."""
    return (h * c / (n * np.pi)) * alpha

# Compute first 10 minimum energy gaps using COM scaling
energy_gaps = [com_energy_gap(n) for n in range(1, 11)]

# Return computed minimum energy gap values for analysis
energy_gaps
Result
[4.618513808438972e-28,
 2.309256904219486e-28,
 1.5395046028129904e-28,
 1.154628452109743e-28,
 9.237027616877943e-29,
 7.697523014064952e-29,
 6.597876869198531e-29,
 5.773142260548715e-29,
 5.131682009376635e-29,
 4.6185138084389715e-29]