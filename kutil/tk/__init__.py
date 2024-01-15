import tkinter
from abc import ABC
from tkinter import ttk


class TkBase(ABC):
    def __init__(self):
        self.tk = tkinter.Tk()

    def mainloop(self):
        self.tk.mainloop()

    def frame(self):
        return Frame(self)


class Frame:
    def __init__(self, parent: TkBase):
        self.frame = ttk.Frame(parent.tk)
