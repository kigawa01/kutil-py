from enum import Enum
from typing import Final

from util.enum.god import God, Gods
from util.enum.star import Star, Stars


####################################################################################################
# 曜日に関するもの
class DayOfWeek:
    """曜日を表します
    :var number: 月曜日を0とした曜日の日数
    :var name: 曜日の名前
    :var star: 曜日の星
    :var god: 曜日の守護神
    :var description: 曜日の占いの詳細
    """
    number: Final[int]
    name: Final[str]
    star: Final[Star]
    god: Final[God]
    description: Final[list[str]]

    def __init__(self, number: int, name: str, star: Stars, god: Gods, description: list[str]):
        self.number = number
        self.name = name
        self.star = star.value
        self.god = god.value
        self.description = description


class DaysOfWeek(Enum):
    """既知の曜日の定義
    :var MON: 月曜日を表す曜日の定義
    :var THU: 火曜日を表す曜日の定義
    :var WHE: 水曜日を表す曜日の定義
    :var THO: 木曜日を表す曜日の定義
    :var FLY: 金曜日を表す曜日の定義
    :var SAT: 土曜日を表す曜日の定義
    :var SUN: 日曜日を表す曜日の定義
    """
    MON = DayOfWeek(0, "月", Stars.MOON, Gods.ARTEMIS, [
        "協調性があり穏やかな癒し系",
        "ロマンチストで感受性が豊か",
        "勤勉家で努力を惜しまないタイプ",
        "論理的よりは感情的で喜怒哀楽が激しい",
    ])
    THU = DayOfWeek(1, "火", Stars.MARS, Gods.MARS, [
        "チャレンジ精神旺盛で行動力がある",
        "頼もしい存在で周囲の人気者",
        "競争心があり強気で負けず嫌い",
        "せっかちで深く考えずに行動しがち",
    ])
    WHE = DayOfWeek(2, "水", Stars.MERCURY, Gods.HERMES, [
        "好奇心が旺盛な知性があるタイプ",
        "器用で発想力豊かなアイディアマン",
        "話上手だが人間関係は広く浅め",
        "飽き性で長続きするのが苦手",
    ])
    THO = DayOfWeek(3, "木", Stars.JUPITER, Gods.ZEUS, [
        "高い集中力で道を切り開ける自信家",
        "挑戦を惜しまないポジティブな心の持ち主",
        "自由を好み風変わりな印象",
        "無関心なことにはアバウトでいい加減",
    ])
    FLY = DayOfWeek(4, "金", Stars.VENUS, Gods.APHRODITE, [
        "美的センスにあふれた華のある存在",
        "明るく楽天的で周囲を明るくさせる",
        "金運がよくセレブに多いタイプ",
        "嫌なことから逃げがちで喜怒哀楽が激しめ",
    ])
    SAT = DayOfWeek(5, "土", Stars.SATURN, Gods.CHRONOS, [
        "忍耐強く努力と責任感に溢れるタイプ",
        "おもてには出さない隠れた野心がある",
        "ペースを乱されることを嫌う",
        "弱音を吐かずストレスを抱え込みがち",
    ])
    SUN = DayOfWeek(6, "日", Stars.SUN, Gods.APOLLO, [
        "周囲を元気にするムードメーカー",
        "主役になれる大きな存在感",
        "自信家でクリエイティブ肌",
        "自己中心的で承認欲求が強め",
    ])

    @staticmethod
    def by_index(index: 0 | 1 | 2 | 3 | 4 | 5 | 6) -> DayOfWeek:
        """月曜日を0とした曜日の日数から曜日の定義を取得する
        :param index: 月曜日を0とした曜日の日数
        :return: 曜日の定義
        :raise ValueError: 存在しない曜日の日数を指定した場合
        """
        for day in DaysOfWeek:
            if day.value.number == index:
                return day.value
        raise ValueError(f"index {index} is not found")

