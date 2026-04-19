# this is the implementation of the simple binary classifier, using perceptron model
import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def activation_function(self, x):
        # Step function
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Convert labels to 0 and 1 (if not already)
        y_ = np.array([1 if i > 0 else 0 for i in y])

        # Training loop
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_pred = self.activation_function(linear_output)

                # Update rule
                update = self.lr * (y_[idx] - y_pred)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([self.activation_function(x) for x in linear_output])
    
# Sample dataset (AND logic)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])  # Yes (1) only when both inputs are 1

# Train perceptron
model = Perceptron(learning_rate=0.1, n_iters=10)
model.fit(X, y)

# Predictions
predictions = model.predict(X)
print("Predictions:", predictions)