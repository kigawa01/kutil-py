from tkinter import Tk

from util.gui.base.misc import MiscElement
from util.gui.base.wm import WmElement


class TKElement(MiscElement[Tk], WmElement[Tk]):
    """TKを保有するクラス
    """
