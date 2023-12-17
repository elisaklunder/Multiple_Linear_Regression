import numpy as np
import logging
from src.multiple_linear_regression import MultipleLinearRegression
from loss_function import LossFunction


class GDMultipleLinearRegression(MultipleLinearRegression):
    def __init__(self, strategy: str = "uniform", num_iterations: int = 1000,
                 alpha: float = 0.1, lambda_param: float = 1.0):
        super().__init__()
        self.strategy = strategy
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.lambda_param = lambda_param
        self._penalty = None

    def _logging(self, i, mse, mae):
        # Configure logging
        logging.basicConfig(
            filename='info_run.log',
            level=logging.INFO,
            format='%(message)s')

        # Logging infos
        logging.info(f"Iteration {i+1}/{self.num_iterations}, mse = {mse},\
 mae = {mae}")

    def _initialize_weights(self, num_weights: int) -> None:
        if self.strategy == "uniform":
            self._weights.append(np.random.uniform(low=-1, high=1,
                                                   size=num_weights))
        if self.strategy == "normal":
            self._weights.append(np.random.normal(loc=0, scale=1,
                                                  size=num_weights))
        self._weights = np.array(self._weights)
        self._weights = np.transpose(self._weights)

    def _loss_gradient(self, X: np.array, y, predicted_y: np.array) \
            -> np.array:
        X_transposed = X.transpose()
        gradient = (1 / len(X)) * np.dot(X_transposed, (predicted_y - y))
        return gradient

    def gradient_descent(self, X, y):
        # Initialize weights based on the chosen strategy
        num_weights = np.shape(X)[1]
        self._initialize_weights(num_weights)

        # Initialize loss object
        loss = LossFunction()

        for i in range(self.num_iterations):

            # Compute the predicted output for each data point
            predicted_y = np.dot(X, self._weights)

            # Compute the gradient
            gradient = self._loss_gradient(X, y, predicted_y)

            # Update the weights
            self._weights = self._weights - self.alpha * gradient

            # Compute the losses
            mae = loss.mean_absolute_error(y, predicted_y)
            mse = loss.mean_squared_error(y, predicted_y, self._penalty,
                                          self._weights, self.lambda_param)

            self._logging(i, mse, mae)

    def train(self, X: np.array = None, y: np.array = None) -> None:
        if X is None:
            raise ValueError("The train slot is empty.")
        if y is None:
            raise ValueError("The target slot is empty.")

        # Reshaping the target to be in matrix form so that there are no
        # broadcasting issues
        y = np.reshape(y, (-1, 1))

        # Add a column of ones to X for the bias term
        n = np.shape(X)[0]
        X = np.c_[np.ones(n), X]

        # Run gd
        self.gradient_descent(X, y)

        self._weights = self._weights.flatten()
