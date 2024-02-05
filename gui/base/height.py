from tkinter import *
from typing import TypeVar, Self

from kutilpy.kutil.gui.base.misc import MiscElement

HeightType = TypeVar("HeightType", bound=Text | Button | Label | Tk | Entry)


class HeightElement(MiscElement[HeightType]):
    """GUIの要素を表すクラス
    """

    def height(self, height: int) -> Self:
        """set height
        """
        self.element.configure(height=height)
        return self
