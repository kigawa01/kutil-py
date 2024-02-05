from tkinter import *
from typing import TypeVar, Self

from kutilpy.kutil.gui.base.misc import MiscElement

WidthType = TypeVar("WidthType", bound=Text | Button | Label | Tk | Entry)


class WidthElement(MiscElement[WidthType]):
    """GUIの要素を表すクラス
    """

    def width(self, width: int) -> Self:
        """widthを指定します
        """
        self.element.configure(width=width)
        return self
