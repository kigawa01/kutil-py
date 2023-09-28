import inspect
from tkinter import *
from typing import TypeVar, Self, Callable, TypedDict

from kutil.kutil.gui.base.misc import MiscElement

CommandType = TypeVar("CommandType", bound=Button)
CommandArgType = TypeVar("CommandArgType", bound=TypedDict)


class CommandElement(MiscElement[CommandType]):
    """GUIの要素を表すクラス
    """

    def command(
            self,
            command: Callable[[Self, CommandArgType], any] | Callable[[Self], any] | Callable[[], any],
            _: type[CommandArgType] = type[TypedDict("", {})],
            args: CommandArgType = None
    ) -> Self:
        """widthを指定します
        """
        signature = inspect.signature(command)
        count = 0
        for parm in signature.parameters.keys():
            if parm == "self":
                continue
            count += 1

        if count == 0:
            func = command
        if count == 1:
            func = (lambda: command(self))
        if count == 2:
            func = (lambda: command(self, args))

        self.element.configure(command=func)
        return self
