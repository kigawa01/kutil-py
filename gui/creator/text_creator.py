from tkinter import Text

from kutil.kutil.gui.base.misc import MiscElement, MiscType
from kutil.kutil.gui.element.text import TextElement


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
