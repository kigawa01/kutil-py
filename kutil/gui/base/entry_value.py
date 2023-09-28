from tkinter import *
from typing import TypeVar

from kutil.kutil.gui.base.misc import MiscElement

EntryValueType = TypeVar("EntryValueType", bound=Entry)


class EntryValueElement(MiscElement[EntryValueType]):
    """GUIの要素を表すクラス
    """

    def entry_value(self) -> str:
        """widthを指定します
        """
        return self.element.get()
