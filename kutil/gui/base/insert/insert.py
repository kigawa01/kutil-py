import tkinter
from typing import TypeVar, Self

from util.gui.base.insert.base import Position
from util.gui.base.insert.positions import Positions
from util.gui.base.misc import MiscElement

InsertType = TypeVar("InsertType", bound=tkinter.Text)


class InsertElement(MiscElement[InsertType]):
    """GUIの要素を表すクラス
    """

    def insert(self, value: str, position: Position = Positions.end()) -> Self:
        """保持するデータをinsertします
        """
        self.element.insert(position.get(), value)
        return self
