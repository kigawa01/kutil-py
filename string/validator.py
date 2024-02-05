import datetime
from typing import TypeVar, Final, final, Any

from kutilpy.kutil.list.immutable_list import ImmutableList
from kutilpy.kutil.string.validator_core import ValidatorInterface, ValidatorInputType, ValidatorParentReturnType, \
    ValidatorReturnType, ValidateError, ChoiceValidatorReturnType


####################################################################################################
# 文字列バリデーター
class ValidatorParent(ValidatorInterface[
                          ValidatorInputType,
                          ValidatorParentReturnType,
                          ValidatorReturnType
                      ]):
    """バリデーターの継承元.
    :var __parent: より上位のバリデーター
    :var __message: バリデーションに失敗した際のメッセージ
    :var __default: 空文字が入力された時の値
    """
    __parent = Final[ValidatorInterface[ValidatorInputType, Any, ValidatorParentReturnType]]
    __message: Final[str]
    __default: str = None

    def __init__(
            self,
            parent: ValidatorInterface[ValidatorInputType, Any, ValidatorParentReturnType] | None,
            message: str | None
    ):
        self.__parent = parent
        self.__message = message

    @final
    def validate(self, s: ValidatorInputType) -> ValidatorReturnType:
        """バリデーションを実行します.
        :param s: バリデーションを行う文字列
        :return: バリデートされた文字列
        :raise ValidateError: バリデーションエラー
        """

        # デフォルトが存在し、sが空文字の場合デフォルトの値を返す
        if (self.__default is not None) and (s == ""):
            return self.__default
        # より上位のバリデーターが存在する場合上位のバリデーションを行う
        if self.__parent is not None:
            s = self.__parent.validate(s)

        # 自身のバリデーションを行い、ValueErrorをcatchした際に、メッセージを格納したValidationErrorをraiseする
        try:
            return self._validate_value(s)
        except ValueError as e:
            self.rise_validate_err(e=e)

    def rise_validate_err(self, message: str | None = None, e: Exception = None):
        """ValidateErrorをraiseする.
        :param message: エラーメッセージ
        :param e: エラー
        :raise ValidateError: バリデーションエラー
        """
        # messageがNoneでない場合それをもとにraiseする
        if message is not None:
            raise ValidateError(message)
        # self.__messageがNoneでない場合それをもとにraiseする
        if self.__message is not None:
            raise ValidateError(self.__message)
        # eがNoneでない場合それをもとにraiseする
        if e is not None:
            raise ValidateError(str(e))
        # すべてNoneの場合空のエラーをraiseする
        raise ValidateError()

    def _validate_value(self, value: ValidatorParentReturnType) -> ValidatorReturnType:
        """バリデーションを行うオーバーライド可能なメソッド.
        :param value: より上位のバリデーターによってバリデーションされた値
        :return: バリデーションを行った値
        """
        raise NotImplementedError()

    def integer(self, message: str = None):
        """整数値のバリデーションを追加します.
        :param message: バリデーションエラーのメッセージ
        :return: 整数値のバリデーター
        """
        return IntValidator[ValidatorInputType, Any](self, message)

    def split(self, message: str = None, separator: str = " "):
        """文字列を分割します.
        :param message: バリデーションエラーのメッセージ
        :param separator: 分割する値
        :return: 整数値のバリデーター
        """
        return SplitValidator[ValidatorInputType](self, separator, message)

    def trim(self, *target: str):
        """文字の端から文字を取り除きます.
        :param target: 取り除く文字列
        :return: トリムするバリデーター
        """
        return TrimValidator[ValidatorInputType](self, target)

    def split_date(self, message: str = None, separator: str = " "):
        """整数値のバリデーションを追加します.
        :param message: バリデーションエラーのメッセージ
        :param separator: 分割する値
        :return: 整数値のバリデーター
        """
        return self.split(separator=separator).list_date(message)

    def choice(self, choices: ImmutableList[ChoiceValidatorReturnType]):
        """選択肢のバリデーション
        :param choices: 選択肢
        """
        return ChoiceValidator[ValidatorInputType, ValidatorParentReturnType, ChoiceValidatorReturnType](
            self,
            choices
        )

    def default(self, default: ValidatorReturnType):
        """デフォルトの値を追加します.
        :param default: 追加する値
        :return: 自身と同一のインスタンス
        """
        self.__default = default
        return self


class TrimValidator(ValidatorParent[ValidatorInputType, str, str]):
    """整数値のバリデーター.
    """
    __target: Final[tuple[str]]

    def __init__(self, parent: ValidatorInterface[
        ValidatorInputType, Any, str
    ], target: tuple[str]):
        super().__init__(parent, None)
        self.__target = target

    def _validate_value(self, value: str) -> str:
        """整数値のバリデーション.
        :param value: 対象の値
        :return: 整数値
        :raise ValueError: 型を変換できなかった場合
        """
        return value.strip(*self.__target)


####################################################################################################
# 選択肢を返すバリデーター

class ChoiceValidatorParent(
    ValidatorParent[ValidatorInputType, ValidatorParentReturnType, ChoiceValidatorReturnType]
):
    """選択肢を返すバリデーターの継承元
    """


class ChoiceValidator(
    ChoiceValidatorParent[ValidatorInputType, ValidatorParentReturnType, ChoiceValidatorReturnType]
):
    """選択肢のバリデーター
    :var __choices: 選択肢のタプル
    """
    __choices: Final[ImmutableList[ChoiceValidatorReturnType]]

    def __init__(
            self,
            parent: ValidatorInterface[ValidatorInputType, Any, ValidatorParentReturnType],
            choices: ImmutableList[ChoiceValidatorReturnType]
    ):
        super().__init__(parent, "選択肢の中から入力してください")
        self.__choices = choices

    def _validate_value(self, value: str) -> ChoiceValidatorReturnType:
        """選択肢のバリデーション.
        :param value: 対象の値
        :return: 選択された選択肢
        :raise ValueError: 選択肢がなかった場合
        """
        result = self.__choices.first_or_none_if(lambda c: c.is_match(value))

        if result is not None:
            return result

        self.rise_validate_err(f"{value}は選択肢に存在しません。")


####################################################################################################
# 整数バリデーター

class IntValidatorParent(ValidatorParent[ValidatorInputType, ValidatorParentReturnType, int]):
    """整数値を扱うバリデーターの継承元.
    """

    def min(self, min_size: int, message: str = None):
        """最小値のバリデーターを追加.
        :param min_size: 最小値
        :param message: バリデーションエラーのメッセージ.
        :return: 整数の最小値のバリデーター
        """
        return IntMinValidator[ValidatorInputType](self, message, min_size)

    def max(self, max_size: int, message: str = None):
        """最大値のバリデーターを追加.
        :param max_size: 最大値
        :param message: バリデーションエラーのメッセージ.
        :return: 整数の最大値のバリデーター
        """
        return IntMaxValidator[ValidatorInputType](self, message, max_size)


class IntValidator(IntValidatorParent[ValidatorInputType, ValidatorParentReturnType]):
    """整数値のバリデーター.
    """

    def __init__(self, parent: ValidatorInterface[
        ValidatorInputType, Any, ValidatorReturnType
    ], message: str | None):
        # 指定がない場合デフォルトのメッセージを使用
        if message is None:
            message = "整数値を入力してください"
        super().__init__(parent, message)

    def _validate_value(self, value: ValidatorParentReturnType) -> ValidatorReturnType:
        """整数値のバリデーション.
        :param value: 対象の値
        :return: 整数値
        :raise ValueError: 型を変換できなかった場合
        """
        return int(value)


class IntMinValidator(IntValidatorParent[ValidatorInputType, int]):
    """整数の最小値のバリデーター.
    :var min_size: 最小値
    """
    min_size: Final[int]

    def __init__(self, parent: ValidatorInterface[
        ValidatorInputType, Any, int
    ], message: str | None, min_size: int):
        self.min_size = min_size
        # 指定がない場合デフォルトのメッセージを使用
        if message is None:
            message = f"{min_size}以上を入力してください"
        super().__init__(parent, message)

    def _validate_value(self, value: int) -> int:
        """整数値のバリデーション.
        :param value: 対象の値
        :return: バリデーションされた値
        :raise ValidateError: 対象範囲外だった場合
        """
        # 比較して対象範囲が外の場合エラーをraise
        if value < self.min_size:
            raise self.rise_validate_err()
        return value


class IntMaxValidator(IntValidatorParent[ValidatorInputType, int]):
    """整数の最大値のバリデーター.
    :var max_size: 最大値
    """
    max_size: Final[int]

    def __init__(self, parent: ValidatorInterface[
        ValidatorInputType, Any, int
    ], message: str | None, min_size: int):
        self.max_size = min_size
        # 指定がない場合デフォルトのメッセージを使用
        if message is None:
            message = f"{min_size}以下を入力してください"
        super().__init__(parent, message)

    def _validate_value(self, value: int) -> int:
        """整数値のバリデーション.
        :param value: 対象の値
        :return: バリデーションされた値
        :raise ValidateError: 対象範囲外だった場合
        """
        # 比較して対象範囲が外の場合エラーをraise
        if value > self.max_size:
            raise self.rise_validate_err()
        return value


####################################################################################################
# リストバリデーター

# バリデーターの返り値を表す型変数
ListReturnType = TypeVar("ListReturnType")

# 親のバリデーターの返り値を表す型変数
ListParentReturnType = TypeVar("ListParentReturnType")


class ListValidatorParent(ValidatorParent[ValidatorInputType, ValidatorParentReturnType, list[ListParentReturnType]]):
    """整数値を扱うバリデーターの継承元.
    """

    def iterate(
            self,
            iterate_validator: ValidatorInterface[ListParentReturnType, Any, ListReturnType],
            message: str = None
    ) -> ValidatorInterface[ValidatorInputType, list[ListParentReturnType], list[ListReturnType]]:
        """リスト内要素のバリデーターを追加
        :param iterate_validator: 要素のバリデーター
        :param message: エラー時のメッセージ
        """
        return IterateValidator[ValidatorInputType, list[ListParentReturnType], list[ListReturnType]](
            self,
            iterate_validator,
            message
        )

    def list_date(self, message: str = None):
        """整数値のバリデーションを追加します.
        :param message: バリデーションエラーのメッセージ
        :return: 整数値のバリデーター
        """
        validator().default("aaa").trim().integer().min(0).max(10)

        return DateValidator(self.iterate(validator().integer()), message)


class SplitValidator(ListValidatorParent[ValidatorInputType, str, list[str]]):
    """分割してリストにするバリデーター.
    :var separator: 分割する値
    """
    separator: Final[str]

    def __init__(self, parent: ValidatorInterface[ValidatorInputType, Any, str], separator: str, message: str | None):
        super().__init__(parent, message)
        self.separator = separator

    def _validate_value(self, value: str) -> list[str]:
        """分割するバリデーション.
        :param value: 対象の値
        :return: 文字列のリスト
        :raise ValueError: 型を変換できなかった場合
        """
        return value.split(self.separator)


class IterateValidator(ListValidatorParent[ValidatorInputType, list[ListParentReturnType], list[ListReturnType]]):
    """リスト要素のバリデーター.
    """
    iterate_validator: Final[ValidatorInterface[ListParentReturnType, Any, ListReturnType]]

    def __init__(
            self,
            parent: ValidatorInterface[
                ValidatorInputType, Any, list[ListParentReturnType]
            ],
            iterate_validator: ValidatorInterface[ListParentReturnType, Any, ListReturnType],
            message: str | None):
        super().__init__(parent, message)
        self.iterate_validator = iterate_validator

    def _validate_value(self, values: list[ListParentReturnType]) -> list[ListReturnType]:
        """整数値のバリデーション.
        :param values: 対象のリスト
        :return: バリデート後のリスト
        :raise ValueError: 型を変換できなかった場合
        """
        result = list[ListReturnType]()
        for value in values:
            result.append(self.iterate_validator.validate(value))

        return result


####################################################################################################
# 日付のバリデーター

class DateValidator(ValidatorParent[ValidatorInputType, list[int], datetime.date]):
    """分割してリストにするバリデーター.
    """

    def __init__(self, parent: ValidatorInterface[ValidatorInputType, Any, list[int]], message: str | None):
        if message is None:
            message = "正しい日付を入力してください"
        super().__init__(parent, message)

    def _validate_value(self, value: list[int]) -> datetime.date:
        """分割するバリデーション.
        :param value: 対象の値
        :return: 文字列のリスト
        :raise ValueError: 型を変換できなかった場合
        """
        if len(value) != 3:
            self.rise_validate_err("年,月,日が必要です")

        return datetime.date(value[0], value[1], value[2])


####################################################################################################
# 空のバリデーター
class EmptyValidator(ValidatorParent[ValidatorInputType, ValidatorInputType, ValidatorInputType]):
    def __init__(self):
        super().__init__(None, None)

    def _validate_value(self, value: ValidatorInputType) -> ValidatorInputType:
        return value


def validator():
    """空のバリデーターを作成.
    :return: 空のバリデーター
    """
    return EmptyValidator()
