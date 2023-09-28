from kutil.kutil.gui.base.insert.base import Position


class IndexPosition(Position):
    """position to insert
    """
    word = 0
    column = 0

    def get(self):
        return f"{self.column}.{self.word}"

    def set_word(self, world: int):
        """set word index
        """
        self.word = world
        return self

    def set_column(self, column: int):
        """set column index
        """
        self.column = column
        return self
