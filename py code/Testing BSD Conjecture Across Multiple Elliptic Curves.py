# Step 4: Testing BSD Conjecture Across Multiple Elliptic Curves

# Define a set of test elliptic curves (coefficients a, b)
test_elliptic_curves = [
    (-1, 1),  # y^2 = x^3 - x + 1
    (-1, 0),  # y^2 = x^3 - x
    (1, 1),   # y^2 = x^3 + x + 1
    (2, -3),  # y^2 = x^3 + 2x - 3
    (-3, 2),  # y^2 = x^3 - 3x + 2
]

# Compute ranks and L(E,1) for each elliptic curve
elliptic_curve_results = []
for coeffs in test_elliptic_curves:
    rank, L_E_1 = elliptic_curve_rank(coeffs, test_range=100)
    elliptic_curve_results.append((coeffs, rank, L_E_1))

# Convert results into a readable format
import pandas as pd
df_elliptic_results = pd.DataFrame(elliptic_curve_results, columns=["Coefficients (a, b)", "Estimated Rank", "L(E,1) Approximation"])

# Display the results
import ace_tools as tools
tools.display_dataframe_to_user(name="Elliptic Curve BSD Results", dataframe=df_elliptic_results)
Result
  Coefficients (a, b)  Estimated Rank  L(E,1) Approximation
0             (-1, 1)               6              0.142857
1             (-1, 0)               1              0.500000
2              (1, 1)               2              0.333333
3             (2, -3)               2              0.333333
4             (-3, 2)              11              0.083333
Elliptic Curve BSD Results