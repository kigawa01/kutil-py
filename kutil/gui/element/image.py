import tkinter
from os import PathLike
from typing import Self

from util.gui.base.element import GUIElement


class ImageElement(
    GUIElement[tkinter.PhotoImage]
):
    """image element
    """

    def file(self, file: str | bytes | PathLike[str] | PathLike[bytes]) -> Self:
        """set image file
        """
        self.element.configure(file=file)
        return self
