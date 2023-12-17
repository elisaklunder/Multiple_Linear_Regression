import numpy as np
from numpy.linalg import norm


class LossFunction:
    def mean_squared_error(
        self,
        y: np.array = [],
        predicted_y: np.array = [],
        penalty: str = None,
        weights: np.array = [],
        lambda_param: float = 0.0,
    ) -> float:
        """
        Args:
            y: np.array containing the ground truth (target values)
            predicted_y: np.array with predicted values of the target
            penalty: string specifying type of penalty
            weights:
            lamba_parameter:
        Raises:

        NEEDS TO BE IMPLEMENED
        Returns:
            float representing the value of the mean square error
        """
        n = np.shape(y)[0]
        sum = 0
        for i in range(n):
            sum += (y[i] - predicted_y[i]) ** 2
        if penalty is None:
            return sum / n
        if penalty == "L1":
            weights = norm(weights, 1)
        if penalty == "L2":
            weights = norm(weights, 2)

        return sum / n + lambda_param * weights

    def mean_absolute_error(self, y, predicted_y):
        n = np.shape(y)[0]
        sum = 0
        for i in range(n):
            sum += abs(y[i] - predicted_y[i])
        return sum / n
