from kutilpy.gui import GuiElement, TkElement
from kutilpy.gui.window_base import WindowBase


class TkButton(TkElement):
    """tkinterのボタンを表す
    """

    def apply_gui_element(self, element):
        element.render()


class Button(GuiElement):
    """ボタン要素を表す
    """

    def render(self) -> TkElement:
        raise NotImplementedError

    def __init__(
            self,
            window: WindowBase,
            text: str | float
    ):
        window = window
        text = text
