from typing import TypeVar

from util.err.errors import SingletonProviderError

SingletonType = TypeVar("SingletonType")


class SingletonProvider:
    """シングルトンクラスを提供します
    """
    singletons: list[any] = []

    def register(self, singleton: any):
        """register singleton
        """
        for s in self.singletons:
            if type(s) == type(singleton):
                raise SingletonProviderError(f"type: {type(singleton)} is already register")

        self.singletons.append(singleton)

    def get(self, singleton_type: type[SingletonType]) -> SingletonType | None:
        """get singleton
        :param singleton_type: singleton type
        """
        for s in self.singletons:
            if type(s) == singleton_type:
                return s

        for s in self.singletons:
            if isinstance(s, singleton_type):
                return s
        return None


Singletons = SingletonProvider()
