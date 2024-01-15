import tkinter
from abc import ABC
from tkinter import ttk
from typing import Self, TypeVar, Generic, Callable

ElementType = TypeVar("ElementType")


class ElementBase(ABC, Generic[ElementType]):
    element: ElementType

    def __init__(self, element: ElementType):
        self.element = element


class WindowBase(
    ElementBase[tkinter.Tk],
    ABC
):
    def __init__(self):
        super().__init__(tkinter.Tk())
        self.min_size(200, 50)
        self.bind("<FocusIn>", self.on_focus)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_focus(self, event):
        pass

    def on_close(self):
        self.destroy()

    def on_destroy(self):
        pass

    def on_mainloop(self):
        pass

    def destroy(self):
        self.on_destroy()
        self.element.destroy()

    def bind(self, sequence: str, func: Callable[[tkinter.Event], object | None]):
        self.element.bind(sequence, func)

    def protocol(self, name: str, func: Callable[[], object | None]):
        self.element.wm_protocol(name, func)

    def lift(self):
        self.element.tkraise()

    def most_front(self, is_enable: bool):
        self.element.wm_attributes("-topmost", is_enable)

    def focus_force(self):
        self.element.focus_force()

    def mainloop(self):
        self.on_mainloop()
        self.element.mainloop()

    def frame(self):
        return Frame(self)

    def button(self):
        return Button(self)

    def min_size(self, width: int, height: int):
        self.element.wm_minsize(
            width=width,
            height=height
        )


PackType = TypeVar("PackType", bound=tkinter.Pack)


class PackBase(
    ElementBase[PackType],
    ABC,
):
    def __init__(self, element: PackType):
        super().__init__(element)

    def pack(self) -> Self:
        self.element.pack()
        return self


class Frame(
    PackBase[tkinter.Frame]
):
    def __init__(self, parent: WindowBase):
        super().__init__(ttk.Frame(parent.element))


class Button(
    PackBase[tkinter.Button]
):
    def __init__(self, parent: WindowBase):
        super().__init__(ttk.Button(parent.element))
