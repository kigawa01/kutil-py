import tkinter

from util.gui.base.misc import MiscElement, MiscType
from util.gui.element.frame import FrameElement


class FrameCreator(MiscElement[MiscType]):
    """ラベルを作成するクラス
    """

    def create_frame(self) -> FrameElement:
        """Frameを作成します。
        """

        frame = tkinter.Button(master=self.element)
        return FrameElement(frame)
