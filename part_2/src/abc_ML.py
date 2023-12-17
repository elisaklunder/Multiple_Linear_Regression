from abc import ABC, abstractmethod


class ML_model(ABC):

    @abstractmethod
    def train():
        pass

    @abstractmethod
    def predict():
        pass

    @property
    @abstractmethod
    def weights():
        pass

    @weights.getter
    @abstractmethod
    def weights():
        pass

    @weights.setter
    @abstractmethod
    def weights():
        pass
