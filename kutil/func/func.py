from typing import Callable, TypeVar, Generic, Final, Self

LambdaType = TypeVar("LambdaType")


class LambdaBase(Generic[LambdaType]):
    """func funcs
    """
    value: Final[LambdaType]

    def __init__(self, value: LambdaType):
        """init class
        """
        self.value = value

    def also(self, func: Callable[[LambdaType], any]) -> Self:
        """func to use own
        """
        func(self.value)
        return self
