from tkinter import Tk

from kutilpy.kutil.gui.base.misc import MiscElement
from kutilpy.kutil.gui.base.wm import WmElement


class TKElement(MiscElement[Tk], WmElement[Tk]):
    """TKを保有するクラス
    """
