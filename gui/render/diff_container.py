from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from kutilpy.gui.render import TkComponent, Component, ComponentBuilder
from kutilpy.list.mutable_dict import MutableDict, KListEntry
from kutilpy.list.mutable_list import MutableList

BuilderType = TypeVar('BuilderType', bound=ComponentBuilder)


class TkDiffContainer(
    Generic[BuilderType],
    ABC
):
    """gui の要素を持つクラス
    """
    tk_components = MutableDict[type, MutableList[TkComponent]]()

    def render(self):
        """レンダリングを行う
        """
        builder = self.builder()
        self.component(builder)

        new_tk_components = MutableDict[type, MutableList[TkComponent]]()
        for new_component in builder.components:
            new_component: Component
            old_tk_list = self.tk_components.get_or_set(type(new_component), lambda: MutableList[TkComponent]())
            tk_component = old_tk_list.first_or_none_if(lambda e: e.key == new_component.key)
            if tk_component is None:
                tk_component = old_tk_list.first_or_none_if(lambda e: e.is_similar(new_component))
            if tk_component is not None:
                old_tk_list.remove(tk_component)
            else:
                tk_component = new_component
            tk_component.apply(new_component)
            new_tk_components.get_or_set(type(new_component), lambda: MutableList[TkComponent]()).append(tk_component)

        for old_tk_list_entry in self.tk_components:
            old_tk_list_entry: KListEntry[type, MutableList[TkComponent]]
            for old_tk_component in old_tk_list_entry.value:
                old_tk_component: TkComponent
                old_tk_component.destroy()

    @abstractmethod
    def builder(self) -> BuilderType:
        raise NotImplementedError

    @abstractmethod
    def component(self, builder: BuilderType):
        raise NotImplementedError
