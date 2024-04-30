import numpy as np
from matplotlib import pyplot as plt
from src.abc_ML import ML_model


class RegressionPlotter:
    @staticmethod
    def _raisingError(_columns: int, _n_features: int) -> None:
        """
        method that raises an error if the number of features in the training
        data and the plotting data don't match

        Args:
            _columns: number of features in the data that needs to be predicted
            _n_features: number of features the model has been trained on

        Raises:
            ValueError: when the model has been trained with n_number of
            features but the data that needs to be plotted has less features
            (_colums). Since we cannot make the assumption of which features
            where chosen by the user, it results in an error.
        """
        if _columns != _n_features:  # should be the same for plot 3d
            raise ValueError(
                f"the number of features of the model \
                             {_n_features} does not match the number of \
                             features of the variable that needs to be \
                             plotted {_columns}"
            )

    @staticmethod
    def _plot_2d(
        _X: np.ndarray, _y: np.ndarray, _slopes: np.ndarray, _n_features: int
    ) -> plt:
        """
        method that plots data in two dimensions

        Args:
            _X: 2d np.ndarray with n colums indicating the features and m rows,
            one for each point
            _y: 1d np.ndarray containing the target value
            _slopes: 1d np.ndarray containing the sopes of the lines that needs
            to be plotted
            _n_features: int indicating the number of features, it produces
            _n_features number of plots

        Raises:
            ValueError: when the model has been trained with n_number of
            features but the data that needs to be plotted has less features
            (_colums).

        Returns:
            2d plot with features in 2 dimensional space and a regression line
        """
        _, _columns = _X.shape
        RegressionPlotter._raisingError(_columns, _n_features)

        fig, axes = plt.subplots(_n_features, 1, figsize=(8, 3 * _n_features))

        for i in range(_n_features):
            # Get values of slope and intercept
            slope = _slopes[i + 1]  # Assuming intercept is stored at index 0
            intercept = _slopes[0]

            # Scatter plot against the target variable
            axes[i].scatter(_X[:, i], _y, label=f"Feature {i + 1}", s=10)

            # Regression line
            line_x = np.linspace(min(_X[:, i]), max(_X[:, i]), 100)
            line_y = slope * line_x + intercept
            axes[i].plot(line_x, line_y, color="red")

            # Axes labeling
            axes[i].set_xlabel(f"Feature {i + 1}")
            axes[i].set_ylabel("Targets")
            axes[i].legend()

        plt.show()

    @staticmethod
    def _plot_3d(_X: np.ndarray, _y: np.ndarray, _slopes: np.ndarray) -> plt:
        """
        method that plots data in three dimensions

        Args:
            X: 2d np.ndarray with n colums indicating the features and m rows,
            one for each point
            y: 1d np.ndarray containing the target value
            slopes: 1d np.aray containing the parameters for plotting the plane

        Returns:
            3d plot with features in 3 dimensional space and a regression plane
        """
        # Plane equation: ax + by + c = z
        a, b = _slopes[1:3]
        c = _slopes[0]

        # Set the figure
        plt.figure(figsize=(8, 8))
        ax = plt.axes(projection="3d")
        ax.grid()

        # Create a meshgrid for the plane
        xx, yy = np.meshgrid(_X[:, 0], _X[:, 1])
        zz = a * xx + b * yy + c

        # Plot the plane
        ax.plot_surface(xx, yy, zz)

        # Plot the dots
        ax.scatter(_X[:, 0], _X[:, 1], _y, s=10)

        # Axes Labels
        ax.set_xlabel("x", labelpad=20)
        ax.set_ylabel("y", labelpad=20)
        ax.set_zlabel("z", labelpad=20)
        plt.show()

    def plot(self, model: ML_model, X: np.ndarray, y: np.ndarray) -> plt:
        """
        method that plots data and the corresponding regression line(s) or
        regression plane for any number of dimensions, given some data and a
        trained regression model

        Args:
            X: 2d np.ndarray with n colums indicating the features and m rows,
            one for each point
            y: 1d np.ndarray containing the target value

        Returns:
            2 or 3 dimensional plots based on the number of features and the
            user's input (when the number of features is == 2)
        """
        slopes = model.weights
        n_features = len(slopes) - 1

        if n_features == 2:
            # let the user choose
            print("For one 3D plot press 1, for two 2D plots press 2: ")
            user_input = int(input())

            # plot one 3d plot
            if user_input == 1:
                self._plot_3d(X, y, slopes)

            # plot two 2D plots
            elif user_input == 2:
                self._plot_2d(X, y, slopes, n_features)

        else:
            self._plot_2d(X, y, slopes, n_features)
