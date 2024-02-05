from typing import TypeVar, Generic

from kutilpy.util import Util

####################################################################################################
# option

OptionType = TypeVar("OptionType")


class Option(Generic[OptionType]):
    __value: OptionType

    def __init__(self, value: OptionType):
        self.__value = value

    def get(self, priority: OptionType = None) -> OptionType:
        return Util.default_on_none(priority, self.__value)

    def set(self, value: OptionType):
        self.__value = value
