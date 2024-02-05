import enum
import random
import typing
from typing import Final

from kutilpy.kutil.list.immutable_list import ImmutableList


class Luck:
    """おみくじの吉を表すクラス
    """
    name: Final[str]
    weight: typing.Final[int]

    def __init__(self, name: str, weight: int = 0):
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return self.name


class Lucks(enum.Enum):
    """既知のおみくじの吉のリスト
    :var DAIKICHI: 大吉を表す吉の定義
    :var KICH: 吉を表す吉の定義
    :var CHUKICHI: 中吉を表す吉の定義
    :var SHOKICHI: 小吉を表す吉の定義
    :var SUEKICHI: 末吉を表す吉の定義
    :var KYO: 凶を表す吉の定義
    :var DAIKYO: 大凶を表す吉の定義
    """
    DAIKICHI = Luck("大吉")
    KICH = Luck("吉")
    CHUKICHI = Luck("中吉")
    SHOKICHI = Luck("小吉")
    SUEKICHI = Luck("末吉")
    KYO = Luck("凶")
    DAIKYO = Luck("大凶")

    @staticmethod
    def get_random(random_obj: random.Random):
        """ランダムな既知を取得します
        :param random_obj: 乱数生成に使用するランダムオブジェクト
        """
        return ImmutableList.by_enum(Lucks) \
            .map(lambda l: l.entry_value, Luck) \
            .random_element(random_obj)
