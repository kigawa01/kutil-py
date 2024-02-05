from abc import ABC

from kutilpy.gui.render.component import Component
from kutilpy.gui.render.tkcomponent import TkComponent
from kutilpy.list.mutable_list import MutableList


class ComponentBuilder(
    ABC
):
    """containerの保持する要素を定義するためのクラス
    :param container:
    :type container: ComponentContainer
    """
    components: MutableList[Component]
    container: any
