# Step 8: Refining the Harmonic Scaling Analysis of COM Mass Gaps

# Compute harmonic integer multiples of COM mass gaps
harmonic_multiples = [n * energy_gaps[0] for n in range(1, 21)]

# Compute closest harmonic multiples to known particle masses
mass_alignment = {
    particle: min(harmonic_multiples, key=lambda x: abs(x - mass))
    for particle, mass in particle_masses.items()
}

# Compute percentage error for alignment
percentage_errors = {
    particle: abs((mass - mass_alignment[particle]) / mass) * 100 for particle, mass in particle_masses.items()
}

# Return refined harmonic mass alignment and errors
mass_alignment, percentage_errors
Result
({'Electron': 9.237027616877944e-27,
  'Up Quark': 9.237027616877944e-27,
  'Down Quark': 9.237027616877944e-27,
  'Neutrino (upper limit)': 9.237027616877944e-27,
  'Muon': 8.313324855190149e-27,
  'Tau': 4.618513808438972e-28},
 {'Electron': 99.99999999998872,
  'Up Quark': 99.99999999991603,
  'Down Quark': 99.99999999996152,
  'Neutrino (upper limit)': 99.99999711342888,
  'Muon': 99.99999999999994,
  'Tau': 100.0})