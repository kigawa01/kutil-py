import tkinter

from util.gui.base.height import HeightElement
from util.gui.base.widget import WidgetElement
from util.gui.base.width import WidthElement


class FrameElement(
    WidthElement[tkinter.Frame],
    HeightElement[tkinter.Frame],
    WidgetElement[tkinter.Frame]
):
    """button element
    """
