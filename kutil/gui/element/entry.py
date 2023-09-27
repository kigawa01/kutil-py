import tkinter

from util.gui.base.entry_value import EntryValueElement
from util.gui.base.height import HeightElement
from util.gui.base.widget import WidgetElement
from util.gui.base.width import WidthElement


class EntryElement(
    EntryValueElement[tkinter.Entry],
    WidthElement[tkinter.Entry],
    HeightElement[tkinter.Entry],
    WidgetElement[tkinter.Entry]
):
    """entry element
    """
