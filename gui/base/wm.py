from tkinter import *
from typing import TypeVar, Self

from kutilpy.gui.base.element import GUIElement

WmType = TypeVar("WmType", bound=Wm)


class WmElement(GUIElement[WmType]):
    """GUIの要素を表すクラス
    """

    def min(self, width: int | None = None, height: int | None = None) -> Self:
        """wmを指定します
        """
        self.element.wm_minsize(width=width, height=height)
        return self

    def geometry(self, width: int, height: int):
        """set window size
        """
        self.element.wm_geometry(f"{width}x{height}")
