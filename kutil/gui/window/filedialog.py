from tkinter import filedialog
from typing import Iterable


class FileDialog:
    """ファイルダイアログを扱うクラス
    """

    @staticmethod
    def open_filename(
            title: str | None = None,
            filetypes: list[tuple[str, str | list[str] | tuple[str, ...]]] | None = None
    ) -> str:
        """ファイルのパスを取得する
        :param title: ダイアログのタイトル
        :param filetypes: ファイルの拡張子
        :return: 取得したファイルパス
        """
        if filetypes is None:
            return filedialog.askopenfilename(title=title)
        else:
            return filedialog.askopenfilename(title=title, filetypes=filetypes)
