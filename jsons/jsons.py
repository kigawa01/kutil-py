import json
from http import client
from typing import Final

JsonType = (
        dict[dict | list | str | int] |
        list[dict | list | str | int] |
        str |
        int
)


class Json:
    """jsonを扱うクラス
    :var json_value: jsonを表す辞書
    """
    json_value: Final[JsonType]

    def __init__(self, json_value: JsonType):
        self.json_value = json_value

    def dumps(self) -> str:
        return json.dumps(self.json_value)

    @staticmethod
    def by_str(json_str: str):
        """文字列からJsonを作成します
        """
        return Json(json.loads(json_str))

    @staticmethod
    def by_response(json_response: client.HTTPResponse):
        """文字列からJsonを作成します
        """
        return Json(json.load(json_response))
