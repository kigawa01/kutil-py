import tkinter

from project.gui.config.fontconfig import FontConfig
from util.gui.base.misc import MiscType, MiscElement
from util.gui.element.label import LabelElement


class LabelCreator(MiscElement[MiscType]):
    """ラベルを作成するクラス
    """

    def create_label(
            self,
            text: float | str,
            pad_row: float | None = None,
            pad_column: float | None = None,
            font_config: FontConfig | None = None,
    ) -> LabelElement:
        """ラベルを作成します
        :param font_config: fontのコンフィグを指定します
        :param pad_row: 最小の幅を指定します
        :param pad_column: 最小高を指定します
        :param text: 表示するテキスト
        :return: 作成したラベル
        """
        args: dict = {
            "master": self.element,
            "text": text
        }
        if pad_row is not None:
            args["padx"] = pad_row
        if pad_column is not None:
            args["pady"] = pad_column
        if font_config is not None:
            args["font"] = font_config.to_font()

        label = tkinter.Label(**args)

        return LabelElement(label)
