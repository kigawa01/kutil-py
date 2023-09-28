from tkinter import *
from typing import TypeVar

from kutil.kutil.gui.base.insert.base import Position
from kutil.kutil.gui.base.insert.positions import Positions
from kutil.kutil.gui.base.misc import MiscElement

TextValueType = TypeVar("TextValueType", bound=Text)


class TextValueElement(MiscElement[TextValueType]):
    """GUIの要素を表すクラス
    """

    def text_value(self, start: Position = Positions.index(), end: Position = Positions.end()) -> str:
        """widthを指定します
        """
        return self.element.get(start.get(), end.get())
