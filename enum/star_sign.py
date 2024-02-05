import datetime
from enum import Enum
from typing import Final


####################################################################################################
# 星座に関するもの

class StarSign:
    """星座を表すクラス
    :var name: 星座の名前
    :var start_month: その星座の始まりの月
    :var start_day: その星座の始まりの日
    """
    name: Final[str]
    start_month: Final[int]
    start_day: Final[int]

    def __init__(self, name: str, start_month: int, start_day: int):
        self.name = name
        self.start_month = start_month
        self.start_day = start_day

    def is_or_more(self, date: datetime.date):
        """指定された日付が星座の最初の日付かよりおそい場合Trueを返します
        :param date: 指定する日付
        :return: TrueまたはFalse
        """
        start_date = datetime.date(date.year, self.start_month, self.start_day)
        return start_date <= date


class StarSigns(Enum):
    """既知の星座の定義
    :var AQUARIUS: みずがめ座を表す星座の定義
    :var PISCES: うお座を表す星座の定義
    :var ARIES: おひつじ座を表す星座の定義
    :var TAURUS: おうし座を表す星座の定義
    :var GEMINI: ふたご座を表す星座の定義
    :var CANCER: かに座を表す星座の定義
    :var LEO: しし座を表す星座の定義
    :var VIRGO: おとめ座を表す星座の定義
    :var LIBRA: てんびん座を表す星座の定義
    :var SCORPIO: さそり座を表す星座の定義
    :var SAGITTARIUS: いて座を表す星座の定義
    :var CAPRICORN: やぎ座を表す星座の定義
    """
    AQUARIUS = StarSign("水瓶座", 1, 20)
    PISCES = StarSign("魚座", 2, 19)
    ARIES = StarSign("牡羊座", 3, 21)
    TAURUS = StarSign("牡牛座", 4, 20)
    GEMINI = StarSign("双子座", 5, 21)
    CANCER = StarSign("蟹座", 5, 22)
    LEO = StarSign("獅子座", 7, 23)
    VIRGO = StarSign("乙女座", 8, 23)
    LIBRA = StarSign("天秤座", 9, 23)
    SCORPIO = StarSign("蠍座", 10, 24)
    SAGITTARIUS = StarSign("射手座", 11, 23)
    CAPRICORN = StarSign("山羊座", 12, 22)

    @staticmethod
    def by_date(date: datetime.date) -> StarSign:
        """指定した日付の星座を取得する
        :param date: 取得する日付
        :return: 指定した日付の星座
        """

        # 日付が遅い順に並んだリストから最初に条件に一致した星座を返す
        for sign in StarSigns.__reversed__():
            if sign.value.is_or_more(date):
                return sign.value
        # 一致するものがなかった場合やぎ座を返す
        return StarSigns.CAPRICORN.value
