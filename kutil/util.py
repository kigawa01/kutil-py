import enum
from typing import TypeVar, Callable

####################################################################################################
# utilityクラス

# ユーティリティで使用する型変数
T = TypeVar("T")

# enumのリストの要素の型
KEnumType = TypeVar("KEnumType", bound=enum.Enum)


class Util:
    """ユーティリティ
    """

    @staticmethod
    def default_on_none(value: T | None, default: T):
        """値がNoneの場合にデフォルトの値を返します
        :param value: 対象の値
        :param default: Noneだった場合のデフォルト値
        :return: None出ない値を返します
        """
        if value is None:
            return default
        return value

    @staticmethod
    def try_none(func: Callable[[], T]) -> T | None:
        """実行した処理で例外が発生した場合Noneを返します
        :param func: 実行する処理
        :return: 処理の返り値またはNone
        """
        # noinspection PyBroadException
        try:
            return func()
        except:
            return None

    @staticmethod
    def try_default(func: Callable[[], T], default: T) -> T:
        """実行した処理で例外が発生した場合デフォルトの値を返します
        :param default: 例外が発生した場合のデフォルト値
        :param func: 実行する処理
        :return: 処理の返り値またはデフォルトの値
        """
        # noinspection PyBroadException
        try:
            return func()
        except:
            return default

    @staticmethod
    def enum_to_list(e: type[KEnumType]) -> list[KEnumType]:
        """enumをリストにします
        """
        result = list[KEnumType]()
        for element in e:
            result.append(element)
        return result

    @staticmethod
    def list_get_or_none(l: list[T], index: int) -> T:
        if len(l) > abs(index) or len(l) == index * -1:
            return l[index]
        return None
