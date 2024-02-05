import datetime


class DateFormatter:
    """日付のフォーマットを行うクラス
    :var format: 日付のフォーマット
    """
    format: str

    def __init__(self, default_format: str = "%Y-%m-%d"):
        self.format = default_format

    def str_to_date(self, str_date: str) -> datetime.date:
        """文字列をdateに変換します
        :param str_date: 日付を表す文字列
        :return: date型で表される日付
        """
        return datetime.datetime.strptime(str_date, self.format).date()

    def date_to_str(self, date: datetime.date) -> str:
        """dateを文字列に変換します
        :param date: 変換する日付
        :return: フォーマットされた日付
        """
        return date.strftime(self.format)
