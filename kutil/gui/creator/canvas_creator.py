import tkinter

from util.gui.base.misc import MiscElement, MiscType
from util.gui.element.canvas import CanvasElement


class CanvasCreator(MiscElement[MiscType]):
    """class of create Canvas
    """

    def create_canvas(
            self,
    ) -> CanvasElement:
        """create Canvas
        """
        return CanvasElement(tkinter.Canvas(master=self.element))
