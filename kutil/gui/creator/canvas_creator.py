import tkinter

from kutil.kutil.gui.base.misc import MiscElement, MiscType
from kutil.kutil.gui.element.canvas import CanvasElement


class CanvasCreator(MiscElement[MiscType]):
    """class of create Canvas
    """

    def create_canvas(
            self,
    ) -> CanvasElement:
        """create Canvas
        """
        return CanvasElement(tkinter.Canvas(master=self.element))
