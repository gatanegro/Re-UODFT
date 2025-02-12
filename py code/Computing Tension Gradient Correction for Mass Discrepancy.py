# Step 9: Computing Tension Gradient Correction for Mass Discrepancy

# Compute the energy difference (tension gradient) between COM predictions and real particle masses
tension_gradient = {
    particle: abs(mass - mass_alignment[particle]) for particle, mass in particle_masses.items()
}

# Compute tension gradient as a percentage of total energy
tension_percentage = {
    particle: (tension_gradient[particle] / mass) * 100 for particle, mass in particle_masses.items()
}

# Return tension gradient values and their percentage contributions
tension_gradient, tension_percentage
Result
({'Electron': 8.187099999999077e-14,
  'Up Quark': 1.0999999999990763e-14,
  'Down Quark': 2.3999999999990763e-14,
  'Neutrino (upper limit)': 3.1999999076297236e-19,
  'Muon': 1.692799999999999e-11,
  'Tau': 2.8464e-10},
 {'Electron': 99.99999999998872,
  'Up Quark': 99.99999999991603,
  'Down Quark': 99.99999999996152,
  'Neutrino (upper limit)': 99.99999711342888,
  'Muon': 99.99999999999994,
  'Tau': 100.0})