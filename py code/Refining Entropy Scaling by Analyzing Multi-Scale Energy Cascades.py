# Step 8: Refining Entropy Scaling by Analyzing Multi-Scale Energy Cascades

# Define a function to compute multi-scale entropy of turbulence intensity
def multi_scale_entropy(data, scale_factor=5):
    """Computes entropy at different spatial scales to analyze turbulence energy cascades."""
    entropies = []
    for scale in range(1, scale_factor + 1):
        scaled_data = data[::scale, ::scale]  # Downsample the data for multi-scale analysis
        entropy_value = compute_entropy(scaled_data)
        entropies.append(entropy_value)
    return entropies

# Compute multi-scale entropy for experimental and COM turbulence
multi_entropy_exp = multi_scale_entropy(turbulence_experimental, scale_factor=10)
multi_entropy_com = multi_scale_entropy(Z_high_reynolds, scale_factor=10)

# Plot multi-scale entropy comparison
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), multi_entropy_exp, marker='o', linestyle='--', label="Experimental Turbulence Entropy")
plt.plot(range(1, 11), multi_entropy_com, marker='s', linestyle='-', label="COM Predicted Turbulence Entropy")

plt.title("Multi-Scale Entropy Analysis of Turbulence Energy Cascades")
plt.xlabel("Scale Factor (Coarse-Graining)")
plt.ylabel("Entropy Value")
plt.legend()
plt.grid(True)
plt.show()

# Return refined entropy scaling results
multi_entropy_exp, multi_entropy_com
Result
([33.68600951967606,
  40.44668149472657,
  38.55352386672882,
  39.45866085941627,
  33.831807539984986,
  31.661261671732483,
  30.136144197782027,
  23.281552359114002,
  20.476765400596406,
  15.363913296836863],
 [24.581535671633986,
  24.570783115682307,
  -36.152156063197936,
  -1.141475304743576,
  -13.078667062041298,
  -36.41934830702804,
  -39.54765546650085,
  -40.59487974819763,
  -111.10732890569844,
  -67.44555117501493])