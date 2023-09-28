from typing import Final

from kutil.kutil.list.immutable_list import ImmutableList


class Advice:
    """おみくじの吉を表すクラス
    """
    name: Final[str]

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def all_advices():
        return ImmutableList(
            "日々の生活を見直し、生活リズムを改善すべし",
        )
