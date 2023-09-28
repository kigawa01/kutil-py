import tkinter

from kutil.kutil.gui.base.misc import MiscElement
from kutil.kutil.gui.component.component import Component
from kutil.kutil.gui.element.frame import FrameElement


class Frame(
    FrameElement,
    Component,
):
    """GUIを扱うクラス。
    """

    def __init__(self, root: MiscElement):
        super().__init__(tkinter.Frame(root.element))
