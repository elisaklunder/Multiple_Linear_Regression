from abc import ABC, abstractmethod


class ML_model(ABC):
    #__init__ ??

    @abstractmethod
    def train():
        pass

    @abstractmethod
    def predict():
        pass

    @property
    @abstractmethod
    def get_weights():
        pass

    @abstractmethod
    def set_weights():
        pass
