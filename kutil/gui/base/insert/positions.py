from util.gui.base.insert.end import EndPosition
from util.gui.base.insert.position import IndexPosition


class Positions:
    """insert positions
    """

    @staticmethod
    def index():
        """index position
        """
        return IndexPosition()

    @staticmethod
    def end():
        """end position
        """
        return EndPosition()
