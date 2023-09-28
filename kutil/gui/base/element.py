from typing import Final, TypeVar, Generic, Self

from kutil.kutil.func.func import LambdaBase

ElementType = TypeVar("ElementType")


class GUIElement(Generic[ElementType], LambdaBase[Self]):
    """GUIの要素を表すクラス
    :var element: gui element
    """
    element: Final[ElementType]

    def __init__(self, element: ElementType):
        """コンストラクタ
        :param element: gui element
        """
        super().__init__(self)
        self.element = element
