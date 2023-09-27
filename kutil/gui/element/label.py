from tkinter import Label
from typing import TypeVar

from util.gui.base.height import HeightElement
from util.gui.base.widget import WidgetElement
from util.gui.base.width import WidthElement

LabelType = TypeVar("LabelType", bound=Label)


class LabelElement(WidthElement[LabelType], HeightElement[LabelType], WidgetElement[LabelType]):
    """label element
    """
