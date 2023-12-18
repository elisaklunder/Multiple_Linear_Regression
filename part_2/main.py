import os
import sys

import numpy as np

sys.path.append(os.getcwd() + "/part_2/src")
from src.gd_multiple_linear_regression import GDMultipleLinearRegression
from src.lasso_regression import LassoRegression
from src.loss_function import LossFunction
from src.model_saver import ModelSaver
from src.multiple_linear_regression import MultipleLinearRegression
from src.regression_plotter import RegressionPlotter
from src.ridge_regression import RidgeRegression

if __name__ == "__main__":
    # Load data
    X = np.load("X.npy")
    y = np.load("y.npy")

    # Split the data into training/testing sets
    X_train = X[:-20]
    X_test = X[-20:]

    # Split the targets into training/testing sets
    y_train = y[:-20]
    y_test = y[-20:]

    # Gradient Descent Multiple Linear Regression
    gd_mlr = GDMultipleLinearRegression()
    gd_mlr.train(X_train, y_train)
    gd_mlr_predictions = gd_mlr.predict(X_test)
    print(
        f"GD Multiple Linear Regression predictions are:\n\
{gd_mlr_predictions}"
    )

    # Lasso
    lasso = LassoRegression()
    lasso.train(X_train, y_train)
    lasso_predictions = lasso.predict(X_test)
    print(f"Lasso predictions are:\n {lasso_predictions}")

    # Ridge
    ridge = RidgeRegression()
    ridge.train(X_train, y_train)
    ridge_predictions = ridge.predict(X_test)
    print(f"Ridge predictions are:\n {ridge_predictions}")

    # Plot Lasso with multiple plots
    plotter = RegressionPlotter()
    plotter.plot(lasso, X_test, y_test)

    # Plot Lasso with two features
    lasso_2features = LassoRegression()
    lasso_2features.train(X_train[:, :2], y_train)
    plotter.plot(lasso_2features, X_test[:, :2], y_test)

    # Save and load weights
    saver = ModelSaver()
    saver.save_weights(ridge, "./weights_ridge.csv")
    mlr = MultipleLinearRegression()
    saver.load_weights(mlr, "./weights_ridge.csv")
    print(f"Predictions with loaded model:\n {mlr.predict(X_test)}")
