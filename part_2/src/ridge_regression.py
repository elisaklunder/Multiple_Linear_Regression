from src.gd_multiple_linear_regression import GDMultipleLinearRegression
import numpy as np


class RidgeRegression(GDMultipleLinearRegression):
    def __init__(self, strategy: str = "uniform", num_iterations: int = 1000,
                 alpha: float = 0.1, lambda_param: float = 1.0):
        super().__init__(strategy, num_iterations, alpha, lambda_param)
        self._penalty = "L2"

    def _loss_gradient(self, X: np.array, y: np.array, predicted_y:
                       np.array) -> np.array:
        n = np.shape(X)[0]
        X_transposed = X.transpose()
        gradient = - (2 / n) * np.dot(X_transposed, (y - predicted_y))
        + 2 * self.lambda_param * self._weights
        return gradient
