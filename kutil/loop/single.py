from typing import Callable, Self


class SingleLoop:
    """main task
    :var next_task: next task
    :var __INSTANCE: Main instance
    """
    next_task: Callable[[], any] | None
    __INSTANCE: Self | None = None

    def __init__(self, first_task: Callable[[], any] | None):
        """init class
        :param first_task: 最初のタスク
        """
        self.next_task = first_task

    def loop(self):
        """main func
        """
        while self.next_task:
            next_task = self.next_task
            self.next_task = None
            next_task()
