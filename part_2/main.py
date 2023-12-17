import numpy as np
import sys
import os
sys.path.append(os.getcwd() + "/part_2/src")
from src.gd_multiple_linear_regression import GDMultipleLinearRegression
from src.lasso_regression import LassoRegression
from src.ridge_regression import RidgeRegression
from src.model_saver import ModelSaver
from sklearn import datasets
from sklearn import linear_model
from src.loss_function import LossFunction


if __name__ == "__main__":

    X, y = datasets.load_diabetes(return_X_y=True)

    # Split the data into training/testing sets
    X_train = X[:-20]
    X_test = X[-20:]

    # Split the targets into training/testing sets
    y_train = y[:-20]
    y_test = y[-20:]

    '''# Our Lasso vs sklearn Lasso
    our_lasso = LassoRegression()
    our_lasso.train(X_train, y_train)
    our_lasso_predictions = our_lasso.predict(X_test)

    sklearn_lasso = linear_model.Lasso()
    sklearn_lasso.fit(X_train, y_train)
    sklearn_lasso_predictions = sklearn_lasso.predict(X_test)

    # Compare lasso predictions
    print(f"Our lasso predictions are:\n {our_lasso_predictions}")
    print(f"Sklearn lasso predictions are:\n {sklearn_lasso_predictions}\n")

    # Our ridge vs sklearn ridge
    our_ridge = RidgeRegression()
    our_ridge.train(X_train, y_train)
    our_ridge_predictions = our_ridge.predict(X_test)

    sklearn_ridge = linear_model.Ridge()
    sklearn_ridge.fit(X_train, y_train)
    sklearn_ridge_predictions = sklearn_ridge.predict(X_test)

    # Compare ridge predictions
    print(f"Our ridge predictions are:\n {our_ridge_predictions}")
    print(f"Sklearn ridge predictions are:\n {sklearn_ridge_predictions}\n")'''

    # Our GD linear regression vs sklearn one
    our_gd_mlr = GDMultipleLinearRegression()
    our_gd_mlr.train(X_train, y_train)
    our_gd_mlr_predictions = our_gd_mlr.predict(X_test)

    sklearn_gd_mlr = linear_model.SGDRegressor()
    loss = LossFunction()
    sklearn_gd_mlr.fit(X_train, y_train)
    sklearn_gd_mlr_predictions = sklearn_gd_mlr.predict(X_test)

    sk_mae = loss.mean_absolute_error(sklearn_gd_mlr_predictions, y_test)
    sk_mse = loss.mean_squared_error(sklearn_gd_mlr_predictions, y_test)
    our_mae = loss.mean_absolute_error(our_gd_mlr_predictions, y_test)
    our_mse = loss.mean_squared_error(our_gd_mlr_predictions, y_test)

    # Compare ridge predictions
    print(f"Our gd_mlr predictions are:\n {our_gd_mlr_predictions}")
    print(f"Sklearn gd_mlr predictions are:\n {sklearn_gd_mlr_predictions}\n")

    print(our_mae, our_mse)
    print(sk_mae, sk_mse)
    # save and load weights
    #saver = ModelSaver()
    #saver.save_weights(our_ridge, "./weights_ridge.csv")
    #mlr = MultipleLinearRegression()
    #saver.load_weights(mlr, "./weights_ridge.csv")
    #print(f"Predictions with loaded model:\n {mlr.predict(X_test)}")
