import tkinter

from kutil.kutil.gui.base.misc import MiscElement
from kutil.kutil.gui.component.component import Component
from kutil.kutil.gui.element.canvas import CanvasElement


class CanvasComponent(
    CanvasElement,
    Component[tkinter.Canvas],
):
    """GUIを扱うクラス。
    """

    def __init__(self, root: MiscElement):
        super().__init__(tkinter.Frame(root._tk_element))
