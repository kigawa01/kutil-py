from abc import ABC

from kutilpy.gui.render.diff_container import TkDiffContainer


class WindowBase(
    TkDiffContainer,
    ABC,
):
    """GUI windowの元となるクラス
    """
