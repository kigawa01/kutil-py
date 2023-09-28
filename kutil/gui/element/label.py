from tkinter import Label
from typing import TypeVar

from kutil.kutil.gui.base.height import HeightElement
from kutil.kutil.gui.base.widget import WidgetElement
from kutil.kutil.gui.base.width import WidthElement

LabelType = TypeVar("LabelType", bound=Label)


class LabelElement(WidthElement[LabelType], HeightElement[LabelType], WidgetElement[LabelType]):
    """label element
    """
