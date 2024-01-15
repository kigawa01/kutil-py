import tkinter
from abc import ABC
from typing import Self, Callable


class ElementBase[T](ABC):
    element: T

    def __init__(self, element: T):
        self.element = element


class MiscBase[T: tkinter.Misc](
    ElementBase[T],
    ABC
):
    def __init__(self, element: T):
        super().__init__(element)
        self.bind("<FocusIn>", self._on_focus)

    def bind(self, sequence: str, func: Callable[[tkinter.Event], object | None]):
        self.element.bind(sequence, func)

    def _on_focus(self, event):
        self.on_focus(event)

    def on_focus(self, event):
        pass

    def on_pre_destroy(self):
        pass

    def destroy(self):
        self.on_pre_destroy()
        self.element.destroy()

    def after(self, milli_sec: int, func: Callable[[], None]):
        self.element.after(milli_sec, func)


class PackBase[T: tkinter.Pack](
    ElementBase[T],
    ABC,
):
    def __init__(self, element: T):
        super().__init__(element)

    def pack(self) -> Self:
        self.element.pack()
        return self


class TkBase(
    MiscBase[tkinter.Tk],
    ABC,
):

    def __init__(self):
        super().__init__(tkinter.Tk())
        self.min_size(200, 50)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()

    def protocol(self, name: str, func: Callable[[], object | None]):
        self.element.wm_protocol(name, func)

    def lift(self):
        self.element.tkraise()

    def most_front(self, is_enable: bool) -> Self:
        self.element.wm_attributes("-topmost", is_enable)
        return self

    def focus_force(self):
        self.element.focus_force()

    def min_size(self, width: int, height: int):
        self.element.wm_minsize(
            width=width,
            height=height
        )
