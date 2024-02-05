from typing import TypeVar, Generic, Callable

from kutilpy.list.mutable_list import MutableList

####################################################################################################
# カスタマイズされた辞書型のユーティリティ

# リストが保持する要素の方
KListType = TypeVar("KListType")
# リストの関数によって返される値の型
KListReturnType = TypeVar("KListReturnType")

# リストの関数によって返される値の型
KDictValueType = TypeVar("KDictValueType")

# リストの関数によって返される値の型
KDictKeyType = TypeVar("KDictKeyType")


class KListEntry(Generic[KDictKeyType, KDictValueType]):
    """辞書型のkeyとvalueをまとめたオブジェクト
    """

    def __init__(self, key: KDictKeyType, value: KDictValueType):
        self.key = key
        self.value = value


class MutableDict(
    Generic[KDictKeyType, KDictValueType],
    MutableList[KListEntry[KDictKeyType, KDictValueType]]
):
    """カスタマイズされた辞書型
    リストの処理に関する関数を提供します
    """

    def get_or_set(self, key: KDictKeyType, factory: Callable[[], KDictValueType]):
        """remove if filter is true
        """
        entry = self.first_or_none_if(lambda e: e.key == key)
        if entry is not None:
            return entry.value
        value = factory()
        self.append(KListEntry(key=key, value=value))
        return value

    def __init__(self, *element: KListType):
        super().__init__(*element)

    def __iter__(self) -> KListType:
        yield from self._elements
