import tkinter

from kutil.kutil.gui.base.height import HeightElement
from kutil.kutil.gui.base.widget import WidgetElement
from kutil.kutil.gui.base.width import WidthElement


class FrameElement(
    WidthElement[tkinter.Frame],
    HeightElement[tkinter.Frame],
    WidgetElement[tkinter.Frame]
):
    """button element
    """
