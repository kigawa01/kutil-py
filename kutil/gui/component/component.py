import tkinter
from abc import abstractmethod
from typing import TypeVar

from util.gui.base.misc import MiscElement
from util.gui.base.widget import WidgetElement
from util.gui.builder.grid import GridBuilder
from util.gui.creator.button_creator import ButtonCreator
from util.gui.creator.canvas_creator import CanvasCreator
from util.gui.creator.entry_creator import EntryCreator
from util.gui.creator.frame_creator import FrameCreator
from util.gui.creator.label_creator import LabelCreator
from util.gui.creator.text_creator import TextCreator
from util.gui.window.filedialog import FileDialog
from util.gui.window.messagebox import MessageBox

ComponentType = TypeVar("ComponentType", bound=tkinter.Tk | tkinter.Frame)


class Component(
    TextCreator[ComponentType],
    CanvasCreator[ComponentType],
    FrameCreator[ComponentType],
    LabelCreator[ComponentType],
    ButtonCreator[ComponentType],
    EntryCreator[ComponentType],
    MessageBox,
    FileDialog,
    GridBuilder,
    WidgetElement[ComponentType],
    MiscElement[ComponentType]
):
    """component for gui
    """

    def __init__(
            self,
            element: ComponentType,
    ):
        super().__init__(element)
        self._setup()

    @abstractmethod
    def _setup(self):
        """GUI表示前のセットアップを実行します
        """
        raise NotImplementedError()
