import enum
from typing import Final

from kutil.kutil.list.immutable_list import ImmutableList


class Choice:
    """選択肢を表すクラス
    """

    def is_match(self, value: any):
        """valueがこの選択肢を表すかを判定します
        :param value: 判定する値
        :return: この選択肢を表す値だった場合Trueを返します
        """
        raise NotImplementedError()


class StringChoice(Choice):
    """文字列の選択肢を表すクラス
    """
    __alies: Final[ImmutableList[str]]
    check_lower: bool

    def __init__(self, *alies: str, check_lower: bool = True):
        self.__alies = ImmutableList(*alies)
        self.check_lower = check_lower

    def is_match(self, value: any):
        """valueがこの選択肢と一致するか判定します
        :param value: 判定する値
        :return: 選択肢の名前と一致した場合Trueを返します
        """
        if self.check_lower:
            return self.__alies.contains_if(lambda s: str(value) == s)
        else:
            return self.__alies.contains_if(lambda s: str(value).lower() == s.lower())


@enum.unique
class YNChoices(enum.Enum, StringChoice):
    """yesまたはnoを表す選択肢
    """
    YES = ["yes", "y"]
    NO = ["no", "n"]

    def __init__(self):
        super(enum.Enum).__init__(self.value[0])
        super(StringChoice).__init__(*self.value, check_lower=False)
