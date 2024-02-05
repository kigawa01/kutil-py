from typing import TypeVar, Callable

from kutilpy.list.immutable_list import ImmutableList

####################################################################################################
# カスタマイズされたリストのユーティリティ

# リストが保持する要素の方
KListType = TypeVar("KListType")
# リストの関数によって返される値の型
KListReturnType = TypeVar("KListReturnType")


class MutableList(ImmutableList[KListType]):
    """カスタマイズされたリスト
    リストの処理に関する関数を提供します
    """

    def append(self, element: KListType):
        """リストの末尾に新たな要素を追加します
        :param element: 追加する要素
        """
        self._elements.append(element)

    def clear(self):
        """中身を空にします
        """
        self._elements.clear()

    def remove_if(self, filter_func: Callable[[KListType], bool]):
        """remove if filter is true
        """
        self.filter(filter_func).for_each(lambda e: self.remove(e))

    def remove(self, element: KListType):
        """remove element
        """
        self._elements.remove(element)
