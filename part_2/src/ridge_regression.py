from lasso_regression import LassoRegression
import numpy as np


class RidgeRegression(LassoRegression):

    def loss_gradient(self, X, y, predicted_y):
        n = np.shape(X)[0]
        X_transposed = X.transpose()
        gradient = - (2 / n) * np.dot(X_transposed, (y - predicted_y))
        + 2 * self.lambda_param * self._weights
        return gradient
