from enum import Enum
from typing import Final


####################################################################################################
# 星に関するもの


class Star:
    """星を表すクラス
    :var name: 星の名前を表す
    """
    name: Final[str]

    def __init__(self, name):
        """コンストラクタ
        :param name: 星の名前
        """
        self.name = name


class Stars(Enum):
    """既知の星の定義
    :var MOON: 月を表す星の定義
    :var MARS: 火星を表す星の定義
    :var MERCURY: 水星を表す星の定義
    :var JUPITER: 木星を表す星の定義
    :var VENUS: 金星を表す星の定義
    :var SATURN: 土星を表す星の定義
    :var SUN: 太陽を表す星の定義
    """
    MOON = Star("月")
    MARS = Star("火星")
    MERCURY = Star("水星")
    JUPITER = Star("木星")
    VENUS = Star("金星")
    SATURN = Star("土星")
    SUN = Star("太陽")
