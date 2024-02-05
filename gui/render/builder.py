from kutilpy.gui.render import ComponentBuilder
from kutilpy.gui.render.component import Component
from kutilpy.gui.render.diff_container import TkDiffContainer
from kutilpy.list.mutable_list import MutableList


class ComponentBuilderImpl(ComponentBuilder):
    components = MutableList[Component]()

    def __init__(self, container: TkDiffContainer):
        self.container = container
