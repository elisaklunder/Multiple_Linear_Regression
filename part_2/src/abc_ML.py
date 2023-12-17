from abc import ABC, abstractmethod
from typing import Any, List


class ML_model(ABC):
    @abstractmethod
    def train(self, X: List[Any]) -> None:
        """
        Args:
            X: data set the model is trained on, it can assume any format
              supported by the model, usually it is a List of values, but they
              can also be formatted in a data frame or np.array.

        Returns:
            None
        """
        pass

    @abstractmethod
    def predict(self, X: Any) -> Any:
        """
        Args:
            X: data to make predictions on, the format must be compatible with
              the model.

        Returns:
            prediction in the format according to the implementation of the
              model
        """
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
