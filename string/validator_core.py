from typing import Generic, TypeVar

from kutilpy.kutil.choice.choice import Choice


####################################################################################################
# validator
# 基礎
# 変数に制限をかける
class ValidateError(Exception):
    """バリデーションに失敗した時のエラー.
    """

    def __init__(self, *args, **kwargs):
        pass


# バリデーターの返り値を表す型変数
ValidatorReturnType = TypeVar("ValidatorReturnType")

# 親のバリデーターの返り値を表す型変数
ValidatorParentReturnType = TypeVar("ValidatorParentReturnType")
# バリデーターへの入力を表す型変数
ValidatorInputType = TypeVar("ValidatorInputType")

# 選択肢を返すバリデーターの正確な型
ChoiceValidatorReturnType = TypeVar("ChoiceValidatorReturnType", bound=Choice)


class ValidatorInterface(Generic[
                             ValidatorInputType,
                             ValidatorParentReturnType,
                             ValidatorReturnType
                         ]):
    """バリデーションを行うクラスを表すインターフェース.
    """

    def validate(self, s: ValidatorInputType) -> ValidatorReturnType:
        """バリデーションを行う.
        :param s: バリデーションを行う文字列
        """
        raise NotImplementedError()

    def _validate_value(self, value: ValidatorParentReturnType) -> ValidatorReturnType:
        """バリデーションを行うオーバーライド可能なメソッド.
        :param value: より上位のバリデーターによってバリデーションされた値
        :return: バリデーションを行った値
        """
        raise NotImplementedError()
