from tkinter import Tk

from kutil.kutil.gui.base.misc import MiscElement
from kutil.kutil.gui.base.wm import WmElement


class TKElement(MiscElement[Tk], WmElement[Tk]):
    """TKを保有するクラス
    """
