
# Step 7: Comparing COM Mass Gaps with Known Fundamental Particle Masses

# Known fundamental particle masses in Joules (converted from electron volts)
particle_masses = {
    "Electron": 8.1871e-14,  # Joules
    "Up Quark": 1.1e-14,  # Approximate
    "Down Quark": 2.4e-14,  # Approximate
    "Neutrino (upper limit)": 3.2e-19,  # Approximate
    "Muon": 1.6928e-11,  # Joules
    "Tau": 2.8464e-10,  # Joules
}

# Compute the ratio of particle masses to COM mass gaps (checking alignment)
mass_comparisons = {particle: mass / energy_gaps[0] for particle, mass in particle_masses.items()}

# Return comparison ratios to analyze alignment
mass_comparisons
Result
{'Electron': 177266981102026.6,
 'Up Quark': 23817185476203.938,
 'Down Quark': 51964768311717.67,
 'Neutrino (upper limit)': 692863577.489569,
 'Muon': 3.66524832491982e+16,
 'Tau': 6.163021521769716e+17}