import logging

import numpy as np
from loss_function import LossFunction
from src.multiple_linear_regression import MultipleLinearRegression


class GDMultipleLinearRegression(MultipleLinearRegression):
    def __init__(
        self,
        strategy: str = "uniform",
        num_iterations: int = 1000,
        alpha: float = 0.1,
        lambda_param: float = 1.0,
    ):
        super().__init__()
        self.strategy = strategy
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.lambda_param = lambda_param
        self._penalty = None

    def _logging(self, i: int, mse: float, mae: float) -> None:
        """
        This private method creates a log file

        Args:
            i (int): integer showing the number of iterations
            mse (float): float with the value of the mean squared error for
            the given iteration
            mae (float): float with the value of the mean absolute error for
            the given iteration
        """
        model_name = None
        if self._penalty is None:
            model_name = "GDMultipleLinearRegression"
        if self._penalty == "L1":
            model_name = "Lasso"
        if self._penalty == "L2":
            model_name = "Ridge"

        logging.basicConfig(
            filename=f"info_{model_name}.log",
            level=logging.INFO,
            format="%(message)s",
        )
        logging.info(
            f"Iteration {i+1}/{self.num_iterations}, mse = {mse}, mae = {mae}"
        )

    def _initialize_weights(self, num_weights: int) -> None:
        """
        This method initializes the weights following a specific distribution
        (either uniform or normal)

        Args:
            num_weights (int): integer representing the number of weights
            to be initialized for gradient descent
        """

        if self.strategy == "uniform":
            self.weight = self.weights.append(
                np.random.uniform(low=-1, high=1, size=num_weights)
            )
        if self.strategy == "normal":
            self.weights = self.weights.append(
                np.random.normal(loc=0, scale=1, size=num_weights)
            )
        self.weights = np.array(self.weights)
        self.weights = np.transpose(self.weights)

    def _loss_gradient(
        self, X: np.array, y, predicted_y: np.array
    ) -> np.array:
        """
        method that computes the loss gradient (the derivative of the loss
        function)

        Args:
            X (np.array): 2d numpy array with n rows (n=number of datapoints)
            and p columns (p=number of parameters)
            y (_type_): 1d numpy array with n rows containing target values
            predicted_y (np.array): _description_

        Returns:
            np.array: np.array with the gradient values
        """

        X_transposed = X.transpose()
        gradient = (1 / len(X)) * np.dot(X_transposed, (predicted_y - y))
        return gradient

    def _gradient_descent(self, X: np.array, y: np.array) -> None:
        """
        method that updates the weights iteratively based on the loss gradient

        Args:
            X (np.array): 2d numpy array with n rows (n=number of datapoints)
            and p columns (p=number of parameters)
            y (np.array): 1d numpy array with n rows containing target values
        """
        # Initialize weights based on the chosen strategy
        num_weights = np.shape(X)[1]
        self._initialize_weights(num_weights)

        # Initialize loss object
        loss = LossFunction()

        for i in range(self.num_iterations):
            # Compute the predicted output for each data point
            predicted_y = np.dot(X, self.weights)

            # Compute the gradient
            gradient = self._loss_gradient(X, y, predicted_y)

            # Update the weights
            self.weights = self.weights - self.alpha * gradient

            # Compute the losses
            mae = loss.mean_absolute_error(y, predicted_y)
            mse = loss.mean_squared_error(
                y, predicted_y, self._penalty, self.weights, self.lambda_param
            )

            self._logging(i, mse, mae)

    def train(self, X: np.array = None, y: np.array = None) -> None:
        """
        public method that carries out the training with gradient descent

        Args:
            X (np.array, optional):  2d numpy array with n rows (n=number of
            datapoints) and p-1 columns (p=number of parameters). Defaults to
            None.
            y (np.array, optional): 1d numpy array with n rows containing
            target values. Defaults to None.

        Raises:
            ValueError: if the X variable is not specified
            ValueError: if the y variable is not specified
        """
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

        # Run gd
        self._gradient_descent(X, y)
        self.weights = self.weights.flatten()
