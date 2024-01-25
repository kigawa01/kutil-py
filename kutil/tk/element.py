import tkinter
from abc import ABC
from concurrent.futures import ThreadPoolExecutor
from tkinter import ttk
from typing import override, Optional, Callable, Self

from kutilpy.kutil.tk.base import MiscBase, PackBase, TkBase


class WindowBase[T: 'WindowBase'](
    TkBase,
    ABC,
):
    parent: Optional['WindowBase'] = None
    _force_focus: bool = False

    def __init__(self, executor: ThreadPoolExecutor):
        super().__init__(executor)
        self.children = list['WindowBase']()

    def is_force_focus(self, force: bool):
        self._force_focus = force

    def mainloop(self):
        self.after(1, self.focus_force)
        self.element.mainloop()

    @override
    def _on_focus(self, event):
        self.focus_force_child()
        super()._on_focus(event)

    def focus_force_child(self):
        reversed_list: list['WindowBase'] = [*self.children]
        reversed_list.reverse()
        for child in reversed_list:
            child: 'WindowBase'
            if not child._force_focus:
                continue
            child.focus_force()
            break

    @override
    def destroy(self):
        for child in self.children:
            child.destroy()

        parent = self.parent
        if parent is not None:
            if parent.children.count(self) != 0:
                parent.children.remove(self)
        super().destroy()

    def frame(self):
        return Frame(self)

    def button(self, text: str):
        return Button(self, text)

    def entry(self):
        return Entry(self)

    def child_window(self, child: 'WindowBase'):
        self.children.append(child)
        child.parent = self


class Frame(
    PackBase[tkinter.Frame],
    MiscBase[tkinter.Frame],
):
    def __init__(self, parent: WindowBase):
        super().__init__(ttk.Frame(parent.element))


class Button(
    PackBase[tkinter.Button],
    MiscBase[tkinter.Button],
):
    _on_click: Callable[[], None] | None = None

    def __init__(self, parent: WindowBase, text: str):
        super().__init__(ttk.Button(
            parent.element,
            text=text,
            command=lambda: self._on_click()
        ))
        self.parent = parent

    def on_click(self, func: Callable[[], any]) -> Self:
        self._on_click = func
        return self

    def on_click_execute(self, func: Callable[[any], any], *args) -> Self:
        self.on_click(lambda: self.parent.execute(func, *args))
        return self


class Entry(
    PackBase[tkinter.Entry],
    MiscBase[tkinter.Entry],
):

    def __init__(self, parent: WindowBase):
        super().__init__(ttk.Entry(
            parent.element,
        ))
        self.parent = parent

    def value(self):
        return self.element.get()
