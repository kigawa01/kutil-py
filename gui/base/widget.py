from tkinter import Widget
from typing import TypeVar

from kutilpy.kutil.gui.base.grid import GridElement
from kutilpy.kutil.gui.base.misc import MiscElement
from kutilpy.kutil.gui.base.pack import PackElement

WidgetType = TypeVar("WidgetType", bound=Widget)


class WidgetElement(
    PackElement[WidgetType],
    GridElement[WidgetType],
    MiscElement[WidgetType],
):
    """GUIの要素を表すクラス
    """
