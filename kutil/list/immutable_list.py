import random
from typing import TypeVar, Final, Generic, Callable, Any

from kutil.kutil.util import KEnumType, Util

# リストが保持する要素の方
KListType = TypeVar("KListType")
# リストの関数によって返される値の型
KListReturnType = TypeVar("KListReturnType")


class ImmutableList(Generic[KListType]):
    """不変のカスタマイズされたリスト
    リストの処理に関する関数を提供します
    :var _elements: リストが保持する要素
    """
    _elements: Final[list[KListType]]

    def contains(self, element: KListType) -> bool:
        """リストに指定された値が含まれる場合Trueを返します
        :var element: チェックする対象の要素
        :return: TrueまたhFalseを返します
        """
        return element in self._elements

    def contains_if(self, func: Callable[[KListType], bool]) -> bool:
        """指定された関数がTrueを返す値が存在する場合はTrueを返します
        :param func: チェックに使用する関数 Callable[[チェックを行う要素], 条件を満たす場合にTrueを返す]
        :return: TrueまたはFalseを返します
        """
        return self.first_or_none_if(func) is not None

    def element_at(self, index: int) -> KListType:
        """指定したインデクスの要素を取り出します
        :param index: 要素を取り出すインデックス
        :return: 取り出した要素
        :raise IndexError: 要素が存在しない場合発生します
        """
        return self._elements[index]

    def element_at_or_else(self, index: int, default: Callable[[int], KListType]) -> KListType:
        """指定したインデクスの要素を取り出します
        要素が存在しない場合デフォルトの関数が実行され、結果を返します
        :param index: 要素を取り出すインデックス
        :param default: 要素が存在しない場合に実行される関数 Callable[[要求されたインデックス], デフォルトとして返答する値]
        :return: 取り出した要素
        """
        if len(self._elements) <= index:
            return default(index)
        return self.element_at(index)

    def element_at_or_none(self, index: int):
        """指定したインデクスの要素を取り出します
        要素が存在しない場合Noneを返します
        :param index: 要素を取り出すインデックス
        :return: 取り出した要素
        """
        return self.element_at_or_else(index, lambda _: None)

    def for_each(self, func: Callable[[KListType], Any]):
        """リストのすべての要素に対して処理を実行します
        :param func: 実行する処理 Callable[[処理を実行する要素], 返り値はありません]
        """
        for e in self:
            func(e)

    def for_each_index(self, func: Callable[[KListType, int], Any]):
        """リストのすべての要素に対してインデックスを使用した処理を実行します
        :param func: 実行する処理 Callable[[処理を実行する要素, 処理を実行する要素のインデックス], 返り値はありません]
        """
        i = 0
        for e in self:
            func(e, i)
            i += 1

    def filter(self, filter_func: Callable[[KListType], bool]):
        """条件を満たす要素で構成されたKListを返します
        この関数は自身の中身を変更しません
        リストの順番が入れ替わることはありません
        :param filter_func: 絞り込む条件を表す関数 Callable[[条件の判定をする要素], 条件を満たす場合Trueを返します]
        :return: 条件を満たした要素で構成されたリスト
        """
        result = list[KListType]()

        for e in self._elements:
            if filter_func(e):
                result.append(e)
        return ImmutableList(*result)

    def first_or_none_if(self, func: Callable[[KListType], bool]) -> KListType | None:
        """条件を満たす最初の値を取得します
        値が存在しない場合はNoneを返します
        :param func: 取得する条件を表す関数 Callable[[条件の判定をする要素], 条件を満たす場合Trueを返します]
        :return: 条件を満たす最初の要素または存在しない場合はNoneを返します
        """
        for e in self._elements:
            if func(e):
                return e

        return None

    def index_of(self, element: KListType) -> int:
        """指定した要素のリスト内のindexを取得します
        要素が存在しない場合は-1を返します
        :param element: 検索する要素
        :return: 要素のindexまたは-1
        """
        i = 0
        for e in self._elements:
            if e == element:
                return i
            i += 1
        return -1

    def join_to_str(self, separator: str, translator: Callable[[KListType, int], str] = lambda s: str(s)) -> str:
        """リストを連結した文字列を返します
        :param separator: 要素の間にはさむ文字列
        :param translator: 要素を文字列に変換する関数
        :return: 要素を連結した文字列
        """
        if self.size() == 0:
            return ""

        result = translator(self.element_at(0), 0)
        for i in range(1, self.size()):
            result += separator + translator(self.element_at(i), i)

        return result

    def map(self, func: Callable[[KListType], KListReturnType], _: type[KListReturnType] = Any):
        """リスト内のすべての要素に対して処理を実行し、結果のリストを返します
        :param func: 実行する処理 Callable[[対象の要素], 処理の結果]
        :param _: KListReturnTypeを指定します
        :return: 結果のリスト
        """
        result = list[KListReturnType]()
        self.for_each(lambda e: result.append(func(e)))
        return ImmutableList(*result)

    def random_element(self, random_obj: random.Random) -> KListType:
        """ランダムな要素を取得します
        :param random_obj: 要素取得に使用するランダムオブジェクト
        :return: ランダムに選ばれたオブジェクト
        """
        return self._elements[random_obj.randint(0, self.size())]

    def size(self) -> int:
        """リストのサイズを取得します
        :return: リストの要素の数
        """
        return len(self._elements)

    def __init__(self, *element: KListType, _: type[KListReturnType] = Any):
        self._elements = list(element)

    def __iter__(self) -> KListType:
        yield from self._elements

    def __str__(self) -> str:
        return self._elements.__str__()

    @staticmethod
    def by_enum(e: type[KEnumType]):
        """enumからリストを作成します
        """
        return ImmutableList(*Util.enum_to_list(e))

    def to_list(self) -> list[KListType]:
        """自身の中身のリストを返します"""
        return [*self._elements]
