# Step 3: Computing Scale-Transformed Mass Gaps

# Define a function to apply scale transformation based on observer’s perspective
def com_mass_gap_scaled(n, lambda_factor=0.02):
    """Transforms the mass gap based on observer's perception scale."""
    return mass_gaps_fractal[n-1] * np.exp(-lambda_factor * n)

# Compute the scale-transformed mass gaps for an observer at different energy scales
mass_gaps_scaled = [com_mass_gap_scaled(n) for n in range(1, 11)]

# Compute new percentage error after applying observational scaling transformation
percentage_error_scaled_mass_gap = [
    abs((com_mass - ym_mass) / ym_mass) * 100 for com_mass, ym_mass in zip(mass_gaps_scaled, yang_mills_mass_gap)
]

# Return scale-transformed mass gaps and percentage error
mass_gaps_scaled, percentage_error_scaled_mass_gap
Result
([5.6505273021757964e-27,
  1.1254854497446534e-26,
  1.6733235974450127e-26,
  2.2056984402692875e-26,
  2.721328041097921e-26,
  3.219626762957936e-26,
  3.70037333967833e-26,
  4.163558604198393e-26,
  4.6093057007385816e-26,
  5.037824197942623e-26],
 [99.89651048897113,
  99.89693356687319,
  99.89784349221948,
  99.89900648167264,
  99.90031765417223,
  99.9017207947815,
  99.90318227787341,
  99.90468043488558,
  99.90620053519052,
  99.90773215754683])