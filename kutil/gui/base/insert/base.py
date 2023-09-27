from abc import abstractmethod


class Position:
    """position
    """

    @abstractmethod
    def get(self):
        """get formatted str
        """
        raise NotImplementedError()
