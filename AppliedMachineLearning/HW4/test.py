# Import necessary libraries
import struct
import numpy as np
import gzip

# Provided function to read IDX files, this is HW4 document example code
def read_idx(filename):
    with gzip.open(filename, 'rb') as f:
        zero, data_type, dims = struct.unpack('>HBB', f.read(4))
        shape = tuple(struct.unpack('>I', f.read(4))[0] for d in range(dims))
        return np.frombuffer(f.read(), dtype=np.uint8).reshape(shape)

# Load the dataset files
train_images = read_idx('./train-images-idx3-ubyte.gz')
train_labels = read_idx('./train-labels-idx1-ubyte.gz')
test_images = read_idx('./t10k-images-idx3-ubyte.gz')
test_labels = read_idx('./t10k-labels-idx1-ubyte.gz')

# Print shapes of data arrays
print(f"Training images shape: {train_images.shape}")
print(f"Training labels shape: {train_labels.shape}")
print(f"Testing images shape: {test_images.shape}")
print(f"Testing labels shape: {test_labels.shape}")

'''
Training images shape: (60000, 28, 28)
Training labels shape: (60000,)
Testing images shape: (10000, 28, 28)
Testing labels shape: (10000,)
'''


# Normalize images
train_images = train_images / 255.0
test_images = test_images / 255.0

# One-hot encode labels
num_classes = 10
train_labels_onehot = np.eye(num_classes)[train_labels]
test_labels_onehot = np.eye(num_classes)[test_labels]

# Set random seed for reproducibility, 20035085 is my student ID
np.random.seed(20035085) 

# Define Sigmoid and Softmax functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def softmax(x):
    e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e_x / e_x.sum(axis=1, keepdims=True)


# Network parameters
input_size = 784
hidden_layer1_size = 128
hidden_layer2_size = 64
output_size = 10

# Initialize weights and biases
weights1 = np.random.uniform(-0.1, 0.1, (input_size, hidden_layer1_size))
bias1 = np.zeros((1, hidden_layer1_size))
weights2 = np.random.uniform(-0.1, 0.1, (hidden_layer1_size, hidden_layer2_size))
bias2 = np.zeros((1, hidden_layer2_size))
weights3 = np.random.uniform(-0.1, 0.1, (hidden_layer2_size, output_size))
bias3 = np.zeros((1, output_size))


def feed_forward(x):
    layer1 = sigmoid(np.dot(x, weights1) + bias1)
    layer2 = sigmoid(np.dot(layer1, weights2) + bias2)
    output_layer = softmax(np.dot(layer2, weights3) + bias3)
    return layer1, layer2, output_layer


# This is the code example from the HW4 document
def categorical_crossentropy(y_true, y_pred):
    # Number of samples
    n_samples = y_true.shape[0]
    # Clip predictions to avoid log(0) errors
    y_pred_clipped = np.clip(y_pred, 1e-12, 1 - 1e-12)
    # Compute cross-entropy loss
    return -np.sum(y_true * np.log(y_pred_clipped)) / n_samples


def backpropagation(x, y_true, layer1, layer2, output_layer):
    # Number of samples
    n_samples = y_true.shape[0]
    
    # Calculate error at output layer
    d_output = output_layer - y_true  # (output_layer - y_true) is the derivative of the cross-entropy loss
    grad_weights3 = np.dot(layer2.T, d_output) / n_samples
    grad_bias3 = np.sum(d_output, axis=0, keepdims=True) / n_samples

    # Calculate error for second hidden layer
    d_layer2 = np.dot(d_output, weights3.T) * sigmoid_derivative(layer2)
    grad_weights2 = np.dot(layer1.T, d_layer2) / n_samples
    grad_bias2 = np.sum(d_layer2, axis=0, keepdims=True) / n_samples

    # Calculate error for first hidden layer
    d_layer1 = np.dot(d_layer2, weights2.T) * sigmoid_derivative(layer1)
    grad_weights1 = np.dot(x.T, d_layer1) / n_samples
    grad_bias1 = np.sum(d_layer1, axis=0, keepdims=True) / n_samples

    # Return the gradients
    return grad_weights1, grad_bias1, grad_weights2, grad_bias2, grad_weights3, grad_bias3


# Hyperparameters
batch_size = 128
epochs = 100
learning_rate = 0.01


# Training loop
for epoch in range(epochs):
    # Shuffle the data
    indices = np.arange(train_images.shape[0])
    np.random.shuffle(indices)
    train_images = train_images[indices]
    train_labels = train_labels[indices]

    train_images = train_images.reshape(-1, 784)
    test_images = test_images.reshape(-1, 784)
    
    # # Mini-batch gradient descent
    for i in range(0, train_images.shape[0], batch_size):
        x_batch = train_images[i:i+batch_size]
        y_batch = train_labels_onehot[i:i+batch_size]

        # Feed forward
        layer1, layer2, output_layer = feed_forward(x_batch)

        # Compute loss (optional, for monitoring training)
        loss = categorical_crossentropy(y_batch, output_layer)

        # Backpropagation to calculate gradients
        grad_weights1, grad_bias1, grad_weights2, grad_bias2, grad_weights3, grad_bias3 = backpropagation(
            x_batch, y_batch, layer1, layer2, output_layer
        )

        # Update parameters
        weights1 -= learning_rate * grad_weights1
        bias1 -= learning_rate * grad_bias1
        weights2 -= learning_rate * grad_weights2
        bias2 -= learning_rate * grad_bias2
        weights3 -= learning_rate * grad_weights3
        bias3 -= learning_rate * grad_bias3

    # Optionally, print the loss to track the training progress
    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")


def predict(x):
    # Forward pass through the trained network
    layer1 = sigmoid(np.dot(x, weights1) + bias1)
    layer2 = sigmoid(np.dot(layer1, weights2) + bias2)
    output_layer = softmax(np.dot(layer2, weights3) + bias3)
    return np.argmax(output_layer, axis=1)

def compute_accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)


# Get predictions for test images
y_test_pred = predict(test_images)
# Convert one-hot encoded test labels back to single integers
y_test_true = test_labels

# Calculate accuracy
accuracy = compute_accuracy(y_test_true, y_test_pred)
print(f"Test Accuracy: {accuracy * 100:.2f}%")


import matplotlib.pyplot as plt

# Identify misclassified images
misclassified_indices = np.where(y_test_pred != y_test_true)[0]

# Plot a few misclassified images
plt.figure(figsize=(10, 10))
for i, idx in enumerate(misclassified_indices[:9]):  # Display up to 9 misclassified images
    plt.subplot(3, 3, i + 1)
    plt.imshow(test_images[idx].reshape(28, 28), cmap='gray')
    plt.title(f"True: {y_test_true[idx]}, Pred: {y_test_pred[idx]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
