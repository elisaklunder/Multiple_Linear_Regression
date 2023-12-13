from src.lasso_regression import LassoRegression
from src.multiple_linear_regression import MultipleLinearRegression
# from src.ridge_regression import RidgeRegression
from src.model_saver import ModelSaver
import numpy as np
from sklearn import datasets
from sklearn import linear_model


if __name__ == "__main__":

    X, y = datasets.load_diabetes(return_X_y=True)

    # Split the data into training/testing sets
    X_train = X[:-20]
    X_test = X[-20:]
    print(X_train)
    # Split the targets into training/testing sets
    y_train = y[:-20]
    y_test = y[-20:]

    # Our Lasso vs sklearn Lasso
    our_lasso = LassoRegression()
    our_lasso.train(X_train, y_train)
    our_w = our_lasso.get_weights()
    shape = np.shape(our_w)
    # print(f"our weights are {our_w}, the shape of it is:{shape}")
    our_predictions = our_lasso.predict(X_test)

    sklearn_lasso = linear_model.Lasso()
    sklearn_lasso.fit(X_train, y_train)
    sklearn_predictions = sklearn_lasso.predict(X_test)

    # Compare predictions
    # print(f"Our predictions are: {our_predictions}")
    # print(f"Sklearn predictions are: {sklearn_predictions}")

    # save and load weights
    saver = ModelSaver()
    # saver.save_weights(our_lasso, "./weights.csv")
    mlr = MultipleLinearRegression()
    # mlr.train(X_train, y_train)
    # print(mlr.get_weights())
    # saver.load_weights(mlr, "./weights.csv")
    # print(f"predictions with loaded model {mlr.predict(X_test)}")
