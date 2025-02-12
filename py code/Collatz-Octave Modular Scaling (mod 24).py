import numpy as np
import matplotlib.pyplot as plt

# Function to compute Collatz-Octave sequence for a given number
def collatz_octave_sequence(n, max_iter=100):
    sequence = [n]
    for _ in range(max_iter):
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Generate Collatz-Octave sequences for visualization
starting_numbers = [7, 15, 27, 51, 99, 133]  # Sample starting numbers
sequences = [collatz_octave_sequence(n) for n in starting_numbers]

# Plot Collatz-Octave sequences
plt.figure(figsize=(10, 6))
for seq, num in zip(sequences, starting_numbers):
    plt.plot(seq, label=f"Start {num}", marker='o', linestyle='--', alpha=0.7)

plt.title("Collatz-Octave Sequences for Different Starting Numbers")
plt.xlabel("Iteration Step")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

# Function to compute COM harmonic scaling
def collatz_modular_scaling(n, mod_base=24):
    """Computes modular residue scaling for COM"""
    return [num % mod_base for num in collatz_octave_sequence(n)]

# Compute COM modular scaling for quantum alignment
modular_sequences = [collatz_modular_scaling(n, mod_base=24) for n in starting_numbers]

# Plot modular scaling
plt.figure(figsize=(10, 5))
for mod_seq, num in zip(modular_sequences, starting_numbers):
    plt.plot(mod_seq, label=f"Start {num}", marker='o', linestyle='--', alpha=0.7)

plt.title("Collatz-Octave Modular Scaling (mod 24)")
plt.xlabel("Iteration Step")
plt.ylabel("Mod 24 Value")
plt.legend()
plt.grid(True)
plt.show()