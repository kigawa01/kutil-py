import tkinter

from util.gui.base.insert.base import Position


class EndPosition(Position):
    """end position to insert
    """

    def get(self):
        return tkinter.END
