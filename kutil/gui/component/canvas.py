import tkinter

from util.gui.base.misc import MiscElement
from util.gui.component.component import Component
from util.gui.element.canvas import CanvasElement


class CanvasComponent(
    CanvasElement,
    Component[tkinter.Canvas],
):
    """GUIを扱うクラス。
    """

    def __init__(self, root: MiscElement):
        super().__init__(tkinter.Frame(root.element))
