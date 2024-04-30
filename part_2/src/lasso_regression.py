import numpy as np
from src.gd_multiple_linear_regression import GDMultipleLinearRegression


class LassoRegression(GDMultipleLinearRegression):
    def __init__(
        self,
        strategy: str = "uniform",
        num_iterations: int = 1000,
        alpha: float = 0.1,
        lambda_param: float = 1.0,
    ):
        super().__init__(strategy, num_iterations, alpha, lambda_param)
        self._penalty = "L1"

    def _loss_gradient(
        self, X: np.ndarray, y, predicted_y: np.ndarray
    ) -> np.ndarray:
        """
        evaluates the gradient with the given loss function (Lasso)

        Args:
            X (np.ndarray): 2d numpy array with n rows (n=number of datapoints)
            and p columns (p=number of parameters)
            y (_type_):  1d numpy array with n rows containing target values
            predicted_y (np.ndarray): 1d numpy array with n rows containing
            predicted target values

        Raises:
        TypeError: when the matrices are not compatible

        Returns:
            np.ndarray:  array containing the values for the gradient
        """
        if np.shape(X)[0] != np.shape(y)[0]:
            raise TypeError("the matrices cannot be multiplied since they \
have uncompatible shapes")
        n = np.shape(X)[0]
        X_transposed = X.transpose()
        gradient = -(2 / n) * np.dot(X_transposed, y - predicted_y)
        +self.lambda_param * np.sign(self._weights)
        return gradient
