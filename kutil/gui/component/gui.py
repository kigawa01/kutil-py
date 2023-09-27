from tkinter import Tk

from util.gui.base.tk import TKElement
from util.gui.component.component import Component


class GUI(
    Component,
    TKElement,
):
    """GUIを扱うクラス。
    """

    def __init__(
            self,
            title: str | None = None,
            tk: Tk | None = None,
            run: bool = True,
            min_width: int = 0,
            min_height: int = 0
    ):
        """
        :param title: GUIのタイトル
        :param tk: 使用するtkinter
        :param run: Trueの場合GUIを表示します。
        :param min_width: 要素の最小幅を指定します
        :param min_height: 要素の最小高を指定します
        """
        if tk is None:
            tk = Tk()

        tk.title = title

        tk.wm_minsize(min_width, min_height)

        super().__init__(tk)

        if run:
            self.run()

    def run(self):
        """GUIを表示します
        """
        self.element.mainloop()
