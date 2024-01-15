import tkinter
from abc import ABC
from tkinter import ttk
from typing import override, Optional

from kutilpy.kutil.tk.base import MiscBase, PackBase, TkBase


class WindowBase[T: 'WindowBase'](
    TkBase,
    ABC,
):
    parent: Optional['WindowBase'] = None
    _force_focus: bool = False

    def __init__(self):
        super().__init__()
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
        print(self.children)
        reversed_list: list['WindowBase'] = [*self.children]
        reversed_list.reverse()
        for child in reversed_list:
            child: 'WindowBase'
            if not child._force_focus:
                continue
            print(child)
            child.focus_force()
            break

    @override
    def destroy(self):
        parent = self.parent
        if parent is not None:
            parent.children.remove(self)
        super().destroy()

    def frame(self):
        return Frame(self)

    def button(self, text: str):
        return Button(self, text)

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
    def __init__(self, parent: WindowBase, text: str):
        super().__init__(ttk.Button(parent.element, text=text))
