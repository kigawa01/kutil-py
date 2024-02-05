import tkinter

from kutil.kutil.gui.base.entry_value import EntryValueElement
from kutil.kutil.gui.base.height import HeightElement
from kutil.kutil.gui.base.widget import WidgetElement
from kutil.kutil.gui.base.width import WidthElement


class EntryElement(
    EntryValueElement[tkinter.Entry],
    WidthElement[tkinter.Entry],
    HeightElement[tkinter.Entry],
    WidgetElement[tkinter.Entry]
):
    """entry element
    """
