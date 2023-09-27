import enum


class WriteMode(enum.Enum):
    """ファイルの書き込みモードを表します
    :var OVERWRITE: 上書き
    :var APPEND: 追記
    """
    OVERWRITE = "w"
    APPEND = "a"
