from abc import ABC

from kutilpy.gui.render import Component


class TkComponent(
    ABC
):
    key: str

    def is_similar(self, other: Component) -> bool:
        if self.key == other.key:
            return True
        return False

    def apply(self, other: Component):
        """Componentを適用します
        """

    def destroy(self):
        """Componentを削除します
        """
