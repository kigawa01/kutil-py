from tkinter import messagebox


class MessageBox:
    """メッセージボックスを扱うクラス
    """

    @staticmethod
    def show_info(
            title: str | None = None,
            message: str | None = None
    ):
        """show message
        :param title: ダイアログのタイトル
        :param message: 表示するメッセージ
        """
        messagebox.showinfo(title, message)

    @staticmethod
    def show_err(
            title: str | None = None,
            message: str | None = None
    ):
        """show error message
        :param title: ダイアログのタイトル
        :param message: 表示するメッセージ
        """
        messagebox.showerror(title, message)
