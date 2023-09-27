from typing import Final, Callable

from util.parent.game import Game
from util.string.matcher import Matcher


####################################################################################################
# アプリケーションの基礎となるもの

class Main:
    """アプリケーションの主となるプログラム.
    :var __yes_matcher: yesを表す文字列の判定を行う
    """
    __yes_matcher: Final[Matcher] = Matcher("y", "yes", "はい")
    __init_game: Final[Callable[[], Game]]

    def __init__(self, init_game: Callable[[], Game]):
        self.__init_game = init_game

    def start(self):
        """プログラムを実行します.
        プログラムの最上位のループ処理を行う
        """
        while True:
            self.__init_game().start()

            if self.__yes_matcher.read_is_match("終了しますか？"):
                break
