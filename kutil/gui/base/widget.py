from tkinter import Widget
from typing import TypeVar

from util.gui.base.grid import GridElement
from util.gui.base.misc import MiscElement
from util.gui.base.pack import PackElement

WidgetType = TypeVar("WidgetType", bound=Widget)


class WidgetElement(
    PackElement[WidgetType],
    GridElement[WidgetType],
    MiscElement[WidgetType],
):
    """GUIの要素を表すクラス
    """
