import tkinter
from abc import abstractmethod
from typing import TypeVar

from kutil.kutil.gui.base.misc import MiscElement
from kutil.kutil.gui.base.widget import WidgetElement
from kutil.kutil.gui.builder.grid import GridBuilder
from kutil.kutil.gui.creator.button_creator import ButtonCreator
from kutil.kutil.gui.creator.canvas_creator import CanvasCreator
from kutil.kutil.gui.creator.entry_creator import EntryCreator
from kutil.kutil.gui.creator.frame_creator import FrameCreator
from kutil.kutil.gui.creator.label_creator import LabelCreator
from kutil.kutil.gui.creator.text_creator import TextCreator
from kutil.kutil.gui.window.filedialog import FileDialog
from kutil.kutil.gui.window.messagebox import MessageBox

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
