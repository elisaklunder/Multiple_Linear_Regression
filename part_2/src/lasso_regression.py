import numpy as np
import logging
from src.multiple_linear_regression import MultipleLinearRegression
from loss_function import LossFunction


class LassoRegression(MultipleLinearRegression):
    def __init__(self, strategy: str = "a", num_iterations: int = 1000, alpha:
                 float = 0.1, lambda_param: float = 2.0):
        super().__init__()
        self.strategy = strategy
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.lambda_param = lambda_param

    def _loss_gradient(self, X: np.array, y, predicted_y: np.array) \
            -> np.array:
        '''
        Args:
            X: 2d numpy array with n rows (n=number of datapoints) and p
            columns (p=number of parameters)
            y: 1d numpy array with n rows containing target values

        Raises:

        Returns:

        '''
        n = np.shape(X)[0]
        X_transposed = X.transpose()
        gradient = - (2 / n) * np.dot(X_transposed, y - predicted_y)
        + self.lambda_param * np.sign(self._weights)
        return gradient

    def _initialize_weights(self, num_weights: int) -> None:
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

        # Initialize weights based on the chosen strategy
        num_weights = np.shape(X)[1]
        self._initialize_weights(num_weights)

        # Configure logging
        logging.basicConfig(
            filename='info_run.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s')

        for i in range(self.num_iterations):

            # Compute the predicted output for each data point
            predicted_y = np.dot(X, self._weights)
            loss = LossFunction()
            mae = loss.mean_absolute_error(y, predicted_y)
            mse = loss.mean_squared_error(y, predicted_y, "l1",
                                          self._weights, self.lambda_param)
            logging.info(f"Iteration {i+1}/{self.num_iterations}")
            logging.info(f"The mean sqared error is:{mse}")
            logging.info(f"The mean absolute error is: {mae}")

            # Compute the gradient
            gradient = self._loss_gradient(X, y, predicted_y)

            # Update the weights
            self._weights = self._weights - self.alpha * gradient

        self._weights = self._weights.flatten()
