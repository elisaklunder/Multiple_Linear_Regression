from lasso_regression import LassoRegression
import numpy as np


class RidgeRegression(LassoRegression):

    def _loss_gradient(self, X: np.array, y: np.array, predicted_y:
                       np.array) -> np.array:
        n = np.shape(X)[0]
        X_transposed = X.transpose()
        gradient = - (2 / n) * np.dot(X_transposed, (y - predicted_y))
        + 2 * self.lambda_param * self._weights
        return gradient
