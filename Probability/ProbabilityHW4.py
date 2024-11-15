import numpy as np
import matplotlib.pyplot as plt
# Part (c) (i)
mu1 = np.array([3, 4])
Sigma1 = np.array([[1, 0], [0, 1]])
# Part (c) (ii)
mu2 = np.array([3, 4])
Sigma2 = np.array([[5, 0.1], [0.2, 0.5]])
# Generate 100 samples of standard normal vectors
Z = np.random.randn(100, 2)
# Cholesky decomposition
L1 = np.linalg.cholesky(Sigma1)
L2 = np.linalg.cholesky(Sigma2)
# Transformations
X1 = mu1 + Z @ L1.T
X2 = mu2 + Z @ L2.T
# Scatter plots
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(X1[:, 0], X1[:, 1], color='blue')
plt.title('Distribution (i)')
plt.xlabel('X1')
plt.ylabel('X2')
plt.subplot(1, 2, 2)
plt.scatter(X2[:, 0], X2[:, 1], color='red')
plt.title('Distribution (ii)')
plt.xlabel('X1')
plt.ylabel('X2')
plt.tight_layout()
plt.show()



