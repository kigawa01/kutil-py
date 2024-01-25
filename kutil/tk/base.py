import threading
import tkinter
import traceback
from abc import ABC
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from typing import Self, Callable, override


class ElementBase[T](ABC):
    element: T

    def __init__(self, element: T):
        self.element = element


class MiscBase[T: tkinter.Misc](
    ElementBase[T],
    ABC
):
    def __init__(self, element: T):
        super().__init__(element)
        self.bind("<FocusIn>", self._on_focus)

    def bind(self, sequence: str, func: Callable[[tkinter.Event], object | None]):
        self.element.bind(sequence, func)

    def _on_focus(self, event):
        self.on_focus(event)

    def on_focus(self, event):
        pass

    def on_pre_destroy(self):
        pass

    def destroy(self):
        self.on_pre_destroy()
        self.element.destroy()

    def after(self, milli_sec: int, func: Callable[[], None]):
        self.element.after(milli_sec, func)


class PackBase[T: tkinter.Pack](
    ElementBase[T],
    ABC,
):
    def __init__(self, element: T):
        super().__init__(element)

    def pack(self) -> Self:
        self.element.pack()
        return self


class ThreadBase[T: tkinter.Misc](
    MiscBase[T],
    ABC,
):

    def __init__(self, element: T, executor: ThreadPoolExecutor):
        super().__init__(element)
        self.executor = executor
        self.sync_tasks = Queue[Callable[[], any]]()
        self.closed = False
        self.lock = threading.Lock()
        self._sync_task_timer()

    def execute(self, func: Callable[[...], any], *args):
        self.executor.submit(self._task, func, *args)

    def _task(self, func: Callable[[...], any], *args):
        # noinspection PyBroadException
        try:
            func(*args)
        except Exception:
            traceback.format_exc()

    def sync(self, func: Callable[[...], any] | Callable[[], any], *args):
        self.sync_tasks.put(lambda: func(*args))

    def _sync_task_timer(self):
        while not self.sync_tasks.empty():
            try:
                self.sync_tasks.get(block=False)()
            except Exception:
                traceback.format_exc()
        self.lock.acquire()
        if not self.closed:
            self.after(100, self._sync_task_timer)
        self.lock.release()

    @override
    def destroy(self):
        self.lock.acquire()
        self.closed = True
        self.lock.release()
        while not self.sync_tasks.empty():
            try:
                self.sync_tasks.get(block=False)()
            except Exception:
                traceback.format_exc()
        super().destroy()


class TkBase(
    ThreadBase[tkinter.Tk],
    ABC,
):

    def __init__(self, executor: ThreadPoolExecutor):
        super().__init__(tkinter.Tk(), executor)
        self.min_size(200, 50)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()

    def protocol(self, name: str, func: Callable[[], object | None]):
        self.element.wm_protocol(name, func)

    def lift(self):
        self.element.tkraise()

    def most_front(self, is_enable: bool) -> Self:
        self.element.wm_attributes("-topmost", is_enable)
        return self

    def focus_force(self):
        self.element.focus_force()

    def min_size(self, width: int, height: int):
        self.element.wm_minsize(
            width=width,
            height=height
        )
