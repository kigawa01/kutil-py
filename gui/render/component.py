from abc import ABC

from kutilpy.gui.render import TkComponent


class Component(
    ABC
):
    key: str

    def create_tk(self) -> TkComponent:
        """TkComponentを作成します
        """
        raise NotImplementedError

