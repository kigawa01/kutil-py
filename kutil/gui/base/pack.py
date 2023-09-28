import tkinter
from typing import TypeVar, Self

from kutil.kutil.gui.base.element import GUIElement

PackType = TypeVar("PackType", bound=tkinter.Pack)


class PackElement(GUIElement[PackType]):
    """GUIの要素を表すクラス
    """

    def pack(self) -> Self:
        """widthを指定します
        """
        self.element.pack_configure()
        return self
