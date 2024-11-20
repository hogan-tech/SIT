import numpy as np


# def monte_carlo_approximation(M):
#     # Generate M samples from the exponential distribution with parameter 5
#     samples = np.random.exponential(1/5, M)
#     # Compute the function values e^{-14 * X_i^2}
#     function_values = np.exp(-14 * samples**2)
#     # Estimate the expectation
#     expectation = np.mean(function_values)
#     # Multiply by 1/5 to get the final approximation
#     approximation = (1/5) * expectation
#     return approximation