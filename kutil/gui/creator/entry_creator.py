import tkinter

from util.gui.base.misc import MiscElement, MiscType
from util.gui.element.entry import EntryElement


class EntryCreator(MiscElement[MiscType]):
    """Entryを作成するクラス
    """

    def create_entry(
            self,
            show: str | None = None
    ) -> EntryElement:
        """ラベルを作成します
        :param show:
        :return: 作成したラベル
        """
        args: dict = {
            "master": self.element,
        }
        if show is not None:
            args["show"] = show

        entry = tkinter.Entry(**args)
        return EntryElement(entry)
