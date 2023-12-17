import numpy as np
from src.abc_ML import ML_model


class MultipleLinearRegression(ML_model):
    def __init__(self) -> None:
        self._weights = []

    def train(self, X: np.array = None, y: np.array = None) -> None:
        '''
        Args:
            X: 2d numpy array with n rows (n=number of datapoints) and p-1
            columns (p=number of parameters)
            y: 1d numpy array with n rows containing target values

        Raises:
            Error when XTX is not invertible

        Returns:
            None
        '''
        if X is None or y is None:
            raise ValueError("The train or the target slot are empty")
        n = np.shape(X)[0]
        X = np.c_[np.ones(n), X]
        X_transposed = X.transpose()
        dot_product = np.dot(X_transposed, X)
        try:
            inverse_dot_product = np.linalg.inv(dot_product)
        except np.linalg.LinAlgError:
            raise np.linalg.LinAlgError("Singular matrix. The matrix X⊤X is \
                                        not invertible. Check your input \
                                        data.")

        self._weights = np.dot(np.dot(inverse_dot_product, X_transposed), y)

    def predict(self, X: np.array = None) -> np.array:
        '''
        Args:
            X: 2d numpy array with n rows (n=number of datapoints) and p-1
            columns (p=number of parameters)

        Raises:
            No errors

        Returns:
            array containing predictions genarated from the X input
        '''
        if X is None:
            raise ValueError("The values that need to be predicted \
                             weren't given")

        n = np.shape(X)[0]
        X = np.c_[np.ones(n), X]
        return np.dot(X, self._weights)

    @property
    def weights(self):
        return self._weights

    @weights.getter
    def weights(self) -> np.array:
        '''
        Args:
            No arguments

        Raises:
            No errors

        Returns:
            An array containing the weights of the model
        '''
        return self._weights

    @weights.setter
    def weights(self, new_weights: np.array) -> None:
        '''
        Args:
            new_weights: array containing value of the weights to be assigned
            to self.weights

        Raises:
            Error if the array contains non numerical values

        Returns:
            None
        '''
        self._weights = new_weights
