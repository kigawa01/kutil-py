from typing import Callable, TypeVar, Generic

ProvideItemType = TypeVar("ProvideItemType")


class ProvideItem(Generic[ProvideItemType]):
    """シングルトンのコンテナ
    :var init: init item func
    :var item: singleton item instance
    """
    init: Callable[[], ProvideItemType]
    item: ProvideItemType | None = None

    def __init__(self, _: type[ProvideItemType], init: Callable[[], ProvideItemType]):
        """init class
        :param init: init item func
        """
        self.init = init

    def get(self) -> ProvideItemType:
        """get singleton item
        """
        if self.item:
            return self.item

        self.item = self.init()
        return self.item
