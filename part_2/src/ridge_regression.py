from lasso_regression import LassoRegression


class RidgeRegression(LassoRegression):

    def loss_gradient(self, X, y, predicted_y):
        n = X.shape()[0]
        X_transposed = X.transpose()
        gradient = - (2/n) * X_transposed * (y - predicted_y)
        + 2 * self.lambda_param * self._weights
        return gradient
