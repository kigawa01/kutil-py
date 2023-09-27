import tkinter

from util.gui.base.misc import MiscElement
from util.gui.component.component import Component
from util.gui.element.frame import FrameElement


class Frame(
    FrameElement,
    Component,
):
    """GUIを扱うクラス。
    """

    def __init__(self, root: MiscElement):
        super().__init__(tkinter.Frame(root.element))
