from tkinter import *
from typing import TypeVar

from util.gui.base.insert.base import Position
from util.gui.base.insert.positions import Positions
from util.gui.base.misc import MiscElement

TextValueType = TypeVar("TextValueType", bound=Text)


class TextValueElement(MiscElement[TextValueType]):
    """GUIの要素を表すクラス
    """

    def text_value(self, start: Position = Positions.index(), end: Position = Positions.end()) -> str:
        """widthを指定します
        """
        return self.element.get(start.get(), end.get())
