from typing import Final

from kutilpy.kutil.string.formatter import Formatter


####################################################################################################
# ゲームの基礎となるもの

class Game:
    """ゲームを表す.
    """
    formatter: Final[Formatter] = Formatter()

    def start(self):
        raise NotImplementedError()
