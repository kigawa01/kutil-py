import tkinter
from os import PathLike

from kutil.kutil.gui.base.height import HeightElement
from kutil.kutil.gui.base.widget import WidgetElement
from kutil.kutil.gui.base.width import WidthElement
from kutil.kutil.gui.element.image import ImageElement


class CanvasElement(
    WidthElement[tkinter.Canvas],
    HeightElement[tkinter.Canvas],
    WidgetElement[tkinter.Canvas]
):
    """Canvas element
    """

    def create_image(
            self,
            file: str | bytes | PathLike[str] | PathLike[bytes]
    ) -> ImageElement:
        """ボタンを作成します。
        """
        image = tkinter.PhotoImage()
        element = ImageElement(image).file(file)
        self.element.create_image((0, 0), image=image, anchor=tkinter.NW)
        return element
