from tkinter import Widget

from util.gui.base.widget import WidgetElement
from util.util import Util


class GridBuilder:
    """GUIを構築するためのクラス
    :var _rows: 構築された行
    """

    _rows = list[list[WidgetElement | None]]()

    def grid_append_row(self, *column_widget: WidgetElement | None):
        """行を追加します
        :param column_widget: 追加するWidget
        """
        row = len(self._rows)
        column_size = self.grid_get_column_size()
        if column_size < len(column_widget):
            column_size = len(column_widget)
            self.grid_set_column_size(column_size)

        for column in range(0, len(column_widget)):
            widget: WidgetElement | None = column_widget[column]
            if widget is None:
                continue
            widget.grid(row=row, column=column)

        if len(column_widget) == 0:
            column_widget = None
        self._rows.append(list(column_widget))
        return self

    def grid_set_column_size(self, size: int):
        """列数を指定します
        :param size: 列数
        """
        for i in range(len(self._rows)):
            row = self._rows[i]
            while len(row) < size:
                row.append(None)
            if len(row) > size:
                self._rows[i] = row[:size]
                for widget in row[size:]:
                    widget.destroy()

    def grid_get_column_size(self) -> int:
        """列数を取得します
        """
        if len(self._rows) == 0:
            return 0
        return len(self._rows[0])

    def grid_set_widget_width(
            self,
            width: float,
            row_indexes: list[int] | int | None = None,
            column_indexes: list[int] | int | None = None,
    ):
        """複数の要素に幅を指定します
        """
        rows = self.grid_get_row(row_indexes)
        if len(rows) == 0:
            return
        if not isinstance(rows[0], list):
            rows: list[list[Widget | None]] = [rows]

        if column_indexes is not None:
            for i in range(len(rows)):
                row = rows[i]
                if isinstance(column_indexes, int):
                    rows[i] = [Util.list_get_or_none(row, column_indexes)]
                    continue
                new_row = list[Widget | None]()
                for column_index in column_indexes:
                    new_row.append(Util.list_get_or_none(row, column_index))
                rows[i] = new_row

        for row in rows:
            for widget in row:
                if widget is None:
                    continue
                widget.configure(**{"width": width})

    def grid_get_row(self, row: list[int] | int | None) -> list[list[Widget | None]] | list[Widget | None]:
        """行を取得します
        """
        if row is None:
            return list(self._rows)
        if isinstance(row, int):
            return Util.list_get_or_none(self._rows, row)

        result = list[list[Widget | None]]()
        for i in row:
            result.append(Util.list_get_or_none(self._rows, i))
        return result
