import tkinter

from kutil.kutil.gui.base.command import CommandElement
from kutil.kutil.gui.base.height import HeightElement
from kutil.kutil.gui.base.widget import WidgetElement
from kutil.kutil.gui.base.width import WidthElement


class ButtonElement(
    CommandElement[tkinter.Button],
    WidthElement[tkinter.Button],
    HeightElement[tkinter.Button],
    WidgetElement[tkinter.Button]
):
    """button element
    """
