from tkinter import Text

from util.gui.base.misc import MiscElement, MiscType
from util.gui.element.text import TextElement


class TextCreator(MiscElement[MiscType]):
    """Text boxを作成するクラス
    """

    def create_text(
            self,
    ) -> TextElement:
        """ラベルを作成します
        :return: 作成したラベル
        """
        text = Text(master=self.element)
        return TextElement(text)
