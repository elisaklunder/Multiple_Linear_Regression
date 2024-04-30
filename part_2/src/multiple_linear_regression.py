import numpy as np
from src.abc_ML import MLModel


class MultipleLinearRegression(MLModel):
    def __init__(self) -> None:
        self._weights = []

    def train(self, X: np.array = None, y: np.array = None) -> None:
        """
        trains the model for multiple linear regression

        Args:
            X (np.array, optional): 2d numpy array with n rows (n=number
            of datapoints) and p-1 columns (p=number of parameters).
            Defaults to None.
            y (np.array, optional): 1d numpy array with n rows
            containing target values. Defaults to None.

        Raises:
            ValueError: if the X or the y slot were not specified
            np.linalg.LinAlgError: when XTX is not invertible
        """
        if X is None or y is None:
            raise ValueError("The train or the target slot are empty")

        n = np.shape(X)[0]
        X = np.c_[np.ones(n), X]
        X_transposed = X.transpose()
        dot_product = np.dot(X_transposed, X)
        try:
            inverse_dot_product = np.linalg.inv(dot_product)
        except np.linalg.LinAlgError:
            raise np.linalg.LinAlgError(
                "Singular matrix. The matrix X⊤X is \
not invertible. Check your input data."
            )

        self.weights = np.dot(np.dot(inverse_dot_product, X_transposed), y)

    def predict(self, X: np.ndarray = None) -> np.ndarray:
        """
        makes predictions on a given np.ndarray

        Args:
            X (np.ndarray, optional): 2d numpy array with n rows (n=number of
            datapoints) and p-1 columns (p=number of parameters). Defaults to
            None.

        Raises:
            ValueError: if the X is not specified

        Returns:
            np.ndarray: array containing predictions genarated from the X input
        """
        if X is None:
            raise ValueError(
                "The values that need to be predicted weren't given"
            )

        n = np.shape(X)[0]
        X = np.c_[np.ones(n), X]
        return np.dot(X, self.weights)

    @property
    def weights(self) -> np.ndarray:
        """
        getter

        Returns:
            np.ndarray: An array containing the weights of the model
        """
        return self._weights

    @weights.setter
    def weights(self, new_weights: np.ndarray) -> None:
        """
        setter

        Args:
            new_weights (np.ndarray): array containing value of the weights
            to be
            assigned to self.weights
        """
        self._weights = new_weights
