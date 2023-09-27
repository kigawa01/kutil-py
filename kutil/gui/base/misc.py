import tkinter
from typing import TypeVar

from util.gui.base.element import GUIElement

MiscType = TypeVar("MiscType", bound=tkinter.Misc)


class MiscElement(
    GUIElement[MiscType],
):
    """GUIの要素を表すクラス
    """

    def __init__(self, element: MiscType):
        """コンストラクタ
        :param element: tkinterの要素
        """
        super().__init__(element)
        self.element.bind("<Configure>", self.__on_configure)
        self.element.bind("<Key>", self.__on_key)
        self.element.bind("<Return>", self.__on_return)

    def __on_configure(self, event: tkinter.Event):
        """configureイベントの処理
        """
        self.on_configure(event)

    def on_configure(self, event: tkinter.Event):
        """configureエベントが発生した際呼び出される
        """

    def __on_key(self, event: tkinter.Event):
        """keyイベントの処理
        """
        self.on_key(event)

    def on_key(self, event: tkinter.Event):
        """keyエベントが発生した際呼び出される
        """

    def __on_return(self, event: tkinter.Event):
        """returnイベントの処理
        """
        self.on_return(event)

    def on_return(self, event: tkinter.Event):
        """keyエベントが発生した際呼び出される
        """

    def destroy(self):
        """destroy element
        """
        self.element.destroy()
