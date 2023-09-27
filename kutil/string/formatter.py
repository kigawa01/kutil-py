from enum import Enum
from typing import Final

from util.string.str_util import StrUtil
from util.tool.option import Option


####################################################################################################
# formatter
# 文字列のフォーマットを行う

class Position(Enum):
    """フォーマッターの文字を寄せる方向を表します.
    :var    LEFT    :左を表します
    :var    CENTER  :中央を表します
    :var    RIGHT   :右を表します
    """
    LEFT = "<"
    CENTER = "^"
    RIGHT = ">"

    def __str__(self):
        return self.value


class Char:
    """1文字を表す.
    :var char: 文字を表す
    """
    char: Final[str]

    def __init__(self, char: str):
        if len(char) != 1:
            raise ValueError("charは一文字でなければいけません")
        self.char = char

    def __str__(self):
        return self.char


class LabelFormatConfig:
    """label_format固有のデフォルトプロパティを保存するクラス
    :var value_position: デフォルトの値の寄せる方向
    """
    label_width: Final[Option[int]]
    value_position: Final[Option[Position]]

    def __init__(self):
        self.value_position = Option(Position.RIGHT)
        self.label_width = Option(10)


class FormatterConfig:
    """フォーマッタのデフォルトプロパティを保存するクラス
    :var width: デフォルトの最大幅
    :var label_format: label_format固有のデフォルトプロパティ
    """
    width: Final[Option[int]]
    label_format: Final[LabelFormatConfig]

    def __init__(self):
        self.width = Option(100)
        self.label_format = LabelFormatConfig()


class Formatter:
    """文字列をフォーマットします.
    :var config: フォーマットに使用するコンフィグ
    """
    config: FormatterConfig

    def __init__(self, config: FormatterConfig = FormatterConfig()):
        self.config = config

    def fill_text(
            self,
            value: any,
            width: int = None,
            blank: Char = Char(" "),
            position: Position = Position.LEFT
    ) -> str:
        """指定した文字列幅になるように補完する.
        :param value: 表示するテキスト
        :param width: 補完後の文字幅(半角文字の数)
        :param blank: 補完する文字
        :param position: 文字を寄せる方向
        """
        # 型の変換
        value = str(value)
        # Noneでない文字列幅の取得
        width = self.config.width.get(width)
        # 全角文字の個数だけ文字列幅を減らします
        width = width - StrUtil.full_width_char_count(value)

        # widthがマイナスの場合0にします
        if width < 0:
            width = 0
        # formatに使う文字列を作成します
        string = f"text:{blank.__str__():.1}{position.__str__():.1}{width:}"
        string = "{" + string + "}"

        # フォーマットを行う
        return string.format(text=value)

    def label_format(
            self,
            label: any,
            value: any,
            separator: any = ": ",
            total_width: int = None,
            label_width: int = None,
            label_position: Position = Position.LEFT,
            value_position: Position = None
    ) -> str:
        """ラベル付きの文字列を文字列から作成する.
        :param value: 表示する値
        :param label: 表示するラベル
        :param separator: ラベルと値を区切る文字
        :param total_width: 合計の文字列の幅
        :param label_width: ラベルの文字列幅
        :param label_position: ラベルの位置
        :param value_position: 値の位置
        """
        # None出ない場合初期値の取得
        total_width = self.config.width.get(total_width)
        value_position = self.config.label_format.value_position.get(value_position)
        label_width = self.config.label_format.label_width.get(label_width)

        # ラベルと値を作成して連結
        return self.fill_text(label, width=label_width, position=label_position) \
            + str(separator) \
            + self.fill_text(value, width=total_width - label_width - 2, position=value_position)

    def label_format_multi(
            self,
            label: any,
            *values: any,
            separator: any = ": ",
            total_width: int = None,
            label_width: int = None,
            label_position: Position = Position.LEFT,
            value_position: Position = None
    ) -> list[str]:
        """ラベル付きの文字列を文字列から作成する.
        :param values: 表示する値
        :param label: 表示するラベル
        :param separator: ラベルと値を区切る文字
        :param total_width: 合計の文字列の幅
        :param label_width: ラベルの文字列幅
        :param label_position: ラベルの位置
        :param value_position: 値の位置
        """
        result = list[str]()
        for value in values:
            result.append(self.label_format(
                label,
                value,
                separator=separator,
                total_width=total_width,
                label_width=label_width,
                label_position=label_position,
                value_position=value_position
            ))
            label = ""
            separator = "  "
        return result

    def splitter(self, message: any = "", width: int = None, blank: Char = Char("_"), prefix: any = "_____") -> str:
        """仕切り.
        :param message: 仕切り上に表示するテキスト
        :param width: 文字列幅
        :param blank: しきりに使う文字
        :param prefix: 先頭に着ける文字列
        """
        # 型の返還
        message = str(message)
        prefix = str(prefix)
        # Noneでない文字列幅の取得
        width = self.config.width.get(width)

        return self.fill_text(f"{prefix}{message}", width, blank=blank, position=Position.LEFT)

    def split_format(
            self,
            *values: any,
            position: Position = Position.LEFT,
            separator: Char = Char(" "),
            width: int = None,
            prefix: any = None,
    ) -> str:
        """複数の文字列を横に分割して表示する.
        :param values: 連結する文字列
        :param position: 文字を寄せる方向
        :param separator: 空白に使用する文字
        :param width: 合計の文字列幅
        :param prefix: 先頭につける文字列
        """
        # Noneでない文字列幅の取得
        width = self.config.width.get(width)

        # prefixがNoneの場合
        if prefix is not None:
            # prefixとprefixの幅を引いたサイズのsplit_formatを連結して返す
            return str(prefix) + self.split_format(
                *values,
                position=position,
                separator=separator,
                width=width - StrUtil.str_width(prefix)
            )

        # 変数の初期化
        result: str = ""
        # 連結する文字列を取り出す
        for value in values:
            # サイズを文字列の数で割った幅にフォーマットしてresultに追加する
            result = result + self.fill_text(
                value,
                width=int(width / len(values)),
                blank=separator,
                position=Position.LEFT
            )
        # サイズの微調整を行って返す
        return self.fill_text(result, width, blank=separator, position=position)
