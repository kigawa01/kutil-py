import tkinter

from kutil.kutil.gui.base.height import HeightElement
from kutil.kutil.gui.base.insert.insert import InsertElement
from kutil.kutil.gui.base.text_value import TextValueElement
from kutil.kutil.gui.base.widget import WidgetElement
from kutil.kutil.gui.base.width import WidthElement


class TextElement(
    TextValueElement[tkinter.Text],
    InsertElement[tkinter.Text],
    WidthElement[tkinter.Text],
    HeightElement[tkinter.Text],
    WidgetElement[tkinter.Text]
):
    """テキストの要素を表す
    """
