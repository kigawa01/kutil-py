from enum import Enum
from typing import Final


####################################################################################################
# 守護神に関するもの

class God:
    """守護神を表すクラス
    :var name: 守護神の名前
    """
    name: Final[str]

    def __init__(self, name: str):
        """コンストラクタ
        :param name: 守護神の名前
        """
        self.name = name


class Gods(Enum):
    """既知の守護神の定義
    :var ARTEMIS: アルテミスを表す守護神の定義
    :var MARS: マースを表す守護神の定義
    :var HERMES: ヘルメスを表す守護神の定義
    :var ZEUS: ゼウスを表す守護神の定義
    :var APHRODITE: アフロディーテを表す守護神の定義
    :var CHRONOS: クロノスを表す守護神の定義
    :var APOLLO: アポロを表す守護神の定義
    """
    ARTEMIS = God("アルテミス")
    MARS = God("マース")
    HERMES = God("ヘルメス")
    ZEUS = God("ゼウス")
    APHRODITE = God("アフロディーテ")
    CHRONOS = God("クロノス")
    APOLLO = God("アポロ")
