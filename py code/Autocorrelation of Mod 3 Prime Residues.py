from scipy.stats import entropy
import seaborn as sns
import pandas as pd

# Compute frequency distribution of mod 3 residues
mod_3_freq = np.bincount(mod_3_residues, minlength=3) / len(mod_3_residues)

# Compute Shannon entropy of mod 3 residue sequence
shannon_entropy = entropy(mod_3_freq, base=2)

# Compute autocorrelation to test periodicity
autocorrelation = np.correlate(mod_3_residues - np.mean(mod_3_residues), mod_3_residues - np.mean(mod_3_residues), mode='full')
autocorrelation = autocorrelation[len(autocorrelation)//2:]  # Keep only positive lags

# Convert data to DataFrame for visualization
df_stats = pd.DataFrame({
    "Residue": [0, 1, 2],
    "Frequency": mod_3_freq
})

# Display statistics and frequency distribution
import ace_tools as tools  
tools.display_dataframe_to_user(name="Mod 3 Residue Statistics", dataframe=df_stats)

# Plot autocorrelation
plt.figure(figsize=(8, 4))
plt.plot(autocorrelation[:20], marker='o', linestyle='-')
plt.title("Autocorrelation of Mod 3 Prime Residues")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)
plt.show()

# Return Shannon entropy and periodicity metrics
shannon_entropy
Result
1.068970776052867