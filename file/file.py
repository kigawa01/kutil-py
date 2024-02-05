from typing import Final, TextIO, TypeVar

from kutilpy.kutil.file.mode import WriteMode

ResultType = TypeVar("ResultType")


class FileIO:
    """ファイルのIOを扱うクラス
    :var filename: ファイル名を表す
    """
    filename: Final[str]

    def __init__(self, filename: str):
        self.filename = filename

    def open(self, write_mode: WriteMode = None, is_read: bool = False) -> TextIO:
        """ファイルのioを開きます
        選択がない場合読み取り専用で開きます
        :param write_mode: 書き込みのモードを選択します
        :param is_read: 読み取るか否かを選択します
        :return: ファイルを扱うio
        """
        mode = ""
        if write_mode is not None:
            mode += write_mode.value

        if is_read:
            mode += "r"

        if mode == "":
            mode = "r"

        return open(self.filename, mode)


class FileReader(FileIO):
    """ファイルを読み取るためのクラス
    """

    def reader(self) -> TextIO:
        """読み取り可能なioを開きます
        :return: 読み取り可能なioを返します
        """
        return self.open(is_read=True)

    def read(self, limit: int = -1, offset: int = 0) -> str:
        """指定したバイト数の文字を読み取ります
        :param limit: 読み取るバイト数を指定します。-1の場合すべて読み取ります。
        :param offset: 読み取る最初のバイトを指定します。
        :return: 読み取った文字列
        """
        with self.reader() as io:
            io.seek(offset)
            return io.read(limit)

    def read_line(self, limit: int = -1) -> str:
        """1行読み取ります
        :param limit: 読み取る最大文字数-1の場合無制限
        :return: 読み取った文字列
        """
        with self.reader() as io:
            return io.readline(limit).strip()

    def read_lines(self) -> list[str]:
        """文字列を読み取り行ごとに分割します
        :return: 読み取った文字列のリスト
        """
        with self.reader() as io:
            return io.readlines()


class FileWriter(FileIO):
    """ファイルの書き込みを行うクラス
    """

    def writer(self, write_mode: WriteMode = WriteMode.OVERWRITE) -> TextIO:
        """ファイルの書き込みを行うioを開きます
        :param write_mode: 書き込みのモードを指定します
        :return: 書き込み可能なIO
        """
        return self.open(write_mode)

    def write(self, content: str, write_mode: WriteMode = WriteMode.OVERWRITE):
        """ファイルに指定された文字列を書き込みます
        :param content: 書き込む内容
        :param write_mode: 書き込みモード
        """
        with self.writer(write_mode) as io:
            io.write(content)

    def write_lines(self, contents: list[str], write_mode: WriteMode = WriteMode.OVERWRITE):
        """ファイルに指定された複数行を書き込みます
        :param contents: 書き込む内容
        :param write_mode: 書き込みモード
        """
        with self.writer(write_mode) as file:
            for content in contents:
                file.write(f"{content}\n")


class File(FileWriter, FileReader, FileIO):
    """ファイルを扱うクラス
    """
