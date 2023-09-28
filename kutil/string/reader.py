from typing import Any

from kutil.kutil.choice.choice import YNChoices
from kutil.kutil.list.immutable_list import ImmutableList
from kutil.kutil.string.validator import ValidatorInterface, ValidatorReturnType, ValidateError, validator


####################################################################################################
# reader
# 入力を読み取るためのもの
# need: validator


class Reader:
    @staticmethod
    def read(message: str, v: ValidatorInterface[str, Any, ValidatorReturnType] = None) -> ValidatorReturnType:
        """文字入力
        :param message: 表示するメッセージ
        :param v: 使用するバリデーター
        """
        # 正常な値が読み取れるまでループ
        while True:
            # 値を読み取る
            s = input(message + "\n")
            # バリデーターがNoneの場合値を返す
            if v is None:
                return s

            # バリデーションを行いValidateErrorが発生した場合メッセージを表示する
            # 成功した場合はその値を返す
            try:
                return v.validate(s)
            except ValidateError as e:
                print(str(e))

    @staticmethod
    def read_yn(message: str) -> bool:
        """yesまたはnoを読み取りyesの場合trueを返します
        :param message: 読み取る際に表示するメッセージ
        :return: yesの場合trueを返します
        """
        return YNChoices.YES == Reader.read(message, validator().choice(ImmutableList.by_enum(YNChoices)))
