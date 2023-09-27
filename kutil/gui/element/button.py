import tkinter

from util.gui.base.command import CommandElement
from util.gui.base.height import HeightElement
from util.gui.base.widget import WidgetElement
from util.gui.base.width import WidthElement


class ButtonElement(
    CommandElement[tkinter.Button],
    WidthElement[tkinter.Button],
    HeightElement[tkinter.Button],
    WidgetElement[tkinter.Button]
):
    """button element
    """
