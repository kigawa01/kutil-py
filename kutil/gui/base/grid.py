from tkinter import *
from typing import TypeVar

from kutil.kutil.gui.base.element import GUIElement

GridType = TypeVar("GridType", bound=Grid)


class GridElement(GUIElement[GridType]):
    """GUIの要素を表すクラス
    """

    def grid(self, row: int, column: int):
        """widthを指定します
        """
        self.element.grid_configure(
            row=row,
            column=column,
        )
        return self
