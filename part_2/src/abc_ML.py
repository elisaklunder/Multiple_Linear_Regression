from abc import ABC, abstractmethod


class ML_model(ABC):

    @abstractmethod
    def train():
        pass

    @abstractmethod
    def predict():
        pass

    @abstractmethod
    def get_weights():
        pass

    @abstractmethod
    def set_weights():
        pass
