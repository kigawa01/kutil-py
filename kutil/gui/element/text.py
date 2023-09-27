import tkinter

from util.gui.base.height import HeightElement
from util.gui.base.insert.insert import InsertElement
from util.gui.base.text_value import TextValueElement
from util.gui.base.widget import WidgetElement
from util.gui.base.width import WidthElement


class TextElement(
    TextValueElement[tkinter.Text],
    InsertElement[tkinter.Text],
    WidthElement[tkinter.Text],
    HeightElement[tkinter.Text],
    WidgetElement[tkinter.Text]
):
    """テキストの要素を表す
    """
