import numpy as np
from src.multiple_linear_regression import MultipleLinearRegression
# from model_saver import ModelSaver


class LassoRegression(MultipleLinearRegression):
    def __init__(self, strategy: str = "a", num_iterations: int = 1000, alpha:
                 float = 0.1, lambda_param: float = 2.0):
        super().__init__()
        self.strategy = strategy
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.lambda_param = lambda_param

    def loss_gradient(self, X, y, predicted_y):
        n = np.shape(X)[0]
        X_transposed = X.transpose()
        gradient = - (2/n) * np.dot(X_transposed, y - predicted_y)
        + self.lambda_param * np.sign(self._weights)
        return gradient

    def train(self, X: np.array = None, y: np.array = None) -> None:
        if X is None or y is None:
            raise ValueError("The train or the target slot are empty")

        # ASK A TA: is it an error of the data or should we handle it??
        y = np.reshape(y, (-1, 1))

        # Add a column of ones to X for the bias term
        n = np.shape(X)[0]
        X = np.c_[np.ones(n), X]

        # Initialize weights based on the chosen strategy
        num_weights = np.shape(X)[1]
        if self.strategy == "a":
            self._weights.append(np.random.uniform(low=-1, high=1,
                                                   size=num_weights))
            self._weights = np.array(self._weights)
            self._weights = np.transpose(self._weights)
        if self.strategy == "b":
            self._weights.append(np.random.normal(loc=0, scale=1,
                                                  size=num_weights))
            self._weights = np.array(self._weights)
            self._weights = np.transpose(self._weights)

        for i in range(self.num_iterations):

            # Compute the predicted output for each data point
            predicted_y = np.dot(X, self._weights)

            # Compute the gradient
            gradient = self.loss_gradient(X, y, predicted_y)

            # Update the weights
            self._weights = self._weights - self.alpha * gradient

        self._weights = self._weights.flatten()
