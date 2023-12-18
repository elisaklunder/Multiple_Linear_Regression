import numpy as np
from numpy.linalg import norm


class LossFunction:
    def mean_squared_error(
        self,
        y: np.ndarray = [],
        predicted_y: np.ndarray = [],
        penalty: str = None,
        weights: np.ndarray = [],
        lambda_param: float = 0.0,
    ) -> float:
        """
        method that evaluates the mean squared error and applies regularization

        Args:
            y (np.ndarray, optional):  np.ndarray containing the ground truth
            (target values). Defaults to [].
            predicted_y (np.ndarray, optional): np.ndarray with predicted
            values of the target. Defaults to [].
            penalty (str, optional): string specifying type of penalty.
            Defaults to None.
            weights (np.ndarray, optional): np.ndarray containing the weights
            that will be regularized. Defaults to [].
            lambda_param (float, optional): regularization parameter. Defaults
            to 0.0.

        Raises:
            ValueError: if the y and predicted_y are empty

        Returns:
            float: representing the value of the mean square error
        """
        if (y == [] or predicted_y == [] or weights == []):
            raise ValueError("The values of y, predicted_y or the weights \
weren't passed to the function")
        n = np.shape(y)[0]
        sum = 0
        for i in range(n):
            sum += (y[i] - predicted_y[i]) ** 2
        if penalty is None:
            return sum / n
        elif penalty == "L1":
            weights = norm(weights, 1)
        elif penalty == "L2":
            weights = norm(weights, 2)
        else:
            raise ValueError("the penality id not defined, the only accepted \
ones are None, L1 or L2")

        return sum / n + lambda_param * weights

    def mean_absolute_error(
            self, y: np.ndarray, predicted_y: np.ndarray
            ) -> float:
        """
        method that evaluates the mean absolute error and applies
        regularization

        Args:
            y (np.ndarray, optional):  np.ndarray containing the ground truth
            (target values).
            predicted_y (np.ndarray, optional): np.ndarray with predicted
            values of the target.

        Raises:
            ValueError: raised when the y or predicted_y arrays are empty

        Returns:
            float: mean absolute error
        """
        if y == [] or predicted_y == []:
            raise ValueError("the y or the predicted_y arrays are empty")

        n = np.shape(y)[0]
        sum = 0
        for i in range(n):
            sum += abs(y[i] - predicted_y[i])
        return sum / n
