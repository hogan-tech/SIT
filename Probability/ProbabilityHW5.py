import numpy as np


def monte_carlo_approximation(M):
    # Generate M samples from the exponential distribution with parameter 5
    samples = np.random.exponential(1/5, M)
    # Compute the function values e^{-14 * X_i^2}
    function_values = np.exp(-14 * samples**2)
    # Estimate the expectation
    expectation = np.mean(function_values)
    # Multiply by 1/5 to get the final approximation
    approximation = (1/5) * expectation
    return approximation


# Run the code for different sample sizes
sample_sizes = [50, 100, 200, 400, 800]
approximations = []
for M in sample_sizes:
    approximation = monte_carlo_approximation(M)
    approximations.append(approximation)
    print(f"Approximation with M={M} samples: {approximation}")
# Reflection on the results
print("\nReflection on the results:")
for i, M in enumerate(sample_sizes):
    print(f"M={M}: Approximation = {approximations[i]}")
