from typing import Final

from kutilpy.kutil.string.reader import Reader
from kutilpy.string.str_util import StrUtil


####################################################################################################
# matcher
# 文字列の一覧を比較する

class Matcher:
    """文字列の一覧を比較する.
    :var targets: 比較対象
    """
    targets: Final[tuple[str]]

    def __init__(self, *targets: str):
        self.targets = targets

    def is_match(self, value: str):
        """自身の比較対象と文字列を比較する.
        :param value: 比較対象
        :return: 自身の比較対象に含まれていた場合Trueを返す
        """
        # 自身の比較対象から取り出す
        for target in self.targets:
            # 双方を小文字にそろえて比較し、同一の場合Trueを返す
            if value.lower() == target.lower():
                return True
        # そうでない場合False
        return False

    def read_is_match(self, message: str):
        """入力を読み取り、自身が表すものに一致する場合Trueを返します.
        :param message: 表示するメッセージ
        """
        return self.is_match(Reader.read(f"{message}[{StrUtil.join_str(*self.targets, sep='/')}]"))
