import csv
import json
import pickle
from pathlib import PurePath

import numpy as np
from src.abc_ML import ML_model


class ModelSaver:
    def save_weights(self, model: ML_model, file_path: str) -> None:
        """
        method that takes care of saving the weights.

        Args:
            model (ML_model): trained model
            file_path (str): string containing the path where the file needs to
            be saved

        Raises:
            NameError: when the file format desired by the user is not
            implemented in the program
        """
        file_format = PurePath(file_path).suffix
        supported_formats = [".csv", ".json", ".pickle"]

        if file_format not in supported_formats:
            raise NameError("The given file format is not supported")

        weights = model.weights

        if file_format == ".csv":
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(weights)

        elif file_format == ".json":
            with open(file_path, "w") as file:
                json.dump({"weights": weights.tolist()}, file)

        elif file_format == ".pickle":
            with open(file_path, "wb") as file:
                pickle.dump(weights, file)

    def load_weights(self, model: ML_model, file_path: str) -> None:
        """
        method that loads weights from a file into a model

        Args:
            model (ML_model): model where the weights need to be loaded
            file_path (str): string containing the path where the file
            containng the weights is located

        Raises:
            NameError: if the format of the file is not supported

        """
        file_format = PurePath(file_path).suffix
        if file_format == ".csv":
            with open(file_path, mode="r") as file:
                reader = csv.reader(file)
                weights = next(reader)
                weights = np.array(weights, dtype=float)
                model.weights = weights

        elif file_format == ".json":
            with open(file_path, "r") as file:
                weights = json.load(file)["weights"]
                weights = np.array(weights, dtype=float)
                model.weights = weights

        elif file_format == ".pickle":
            with open(file_path, "rb") as file:
                weights = pickle.load(file)
                weights = np.array(weights, dtype=float)
                model.weights = weights

        else:
            raise NameError("The format of the file is not supported")
