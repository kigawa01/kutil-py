import tkinter

from kutil.kutil.gui.base.misc import MiscElement, MiscType
from kutil.kutil.gui.element.button import ButtonElement


class ButtonCreator(MiscElement[MiscType]):
    """ラベルを作成するクラス
    """

    def create_button(
            self,
            text: float | str,
    ) -> ButtonElement:
        """ボタンを作成します。
        """
        return ButtonElement(tkinter.Button(master=self.element, text=text))
