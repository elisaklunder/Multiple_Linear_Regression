import numpy as np
import csv
import json
import pickle
from pathlib import PurePath
from src.abc_ML import ML_model


class ModelSaver:

    def save_weights(self, model: ML_model, file_path: str) -> None:
        '''
        Args:
            model: trained model, assuming that to get the weights the model
            has a method called get_weights()
            file_path: string containing the path where the file needs to be
            saved

        Raises:
            NameError when the file format desired by the user is not
            implemented in the program

        Returns:
            None
        '''
        file_format = PurePath(file_path).suffix
        supported_formats = [".csv", ".json", ".pickle"]

        if file_format not in supported_formats:
            raise NameError("The given file format is not supported")

        weights = model.get_weights()

        if file_format == '.csv':
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(weights)

        elif file_format == '.json':
            with open(file_path, 'w') as file:
                json.dump({'weights': weights.tolist()}, file)

        elif file_format == '.pickle':
            with open(file_path, 'wb') as file:
                pickle.dump(weights, file)

    def load_weights(self, model: ML_model, file_path: str) -> None:
        '''
        Args:
            model: model where the weights need to be loaded, assuming that to
            set the weights the model has a method called set_weights()
            file_path: string containing the path where the file containng the
            weghts is located

        Raises:
            No errors are raised

        Returns:
            None
        '''
        file_format = PurePath(file_path).suffix
        if file_format == '.csv':
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                weights = next(reader)
                weights = np.array(weights, dtype=float)
                model.set_weights(weights)

        elif file_format == '.json':
            with open(file_path, 'r') as file:
                weights = json.load(file)['weights']
                weights = np.array(weights, dtype=float)
                model.set_weights(weights)

        elif file_format == '.pickle':
            with open(file_path, 'rb') as file:
                weights = pickle.load(file)
                weights = np.array(weights, dtype=float)
                model.set_weights(weights)