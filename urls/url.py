from typing import Final, Self
from urllib import parse


####################################################################################################
# urlに関するもの

class URL:
    """urlを扱うためのクラス
    :var parse_result: urlの情報
    """
    parse_result: Final[parse.ParseResult]

    def __init__(self, parse_result: parse.ParseResult):
        self.parse_result = parse_result

    @staticmethod
    def by_str(url: str):
        """文字列のurlからURLオブジェクトを作成します
        :param url: 文字列のurl
        """
        result = parse.urlparse(url)
        return URL(result)

    def join_path(self, path: str) -> Self:
        """既存のurlにpathを追加します
        :param path: 追加するpath
        """
        path = parse.urljoin(self.parse_result.path, path)
        self.parse_result._replace(path=path)
        return self

    def join_query(self, query: dict[str, str]) -> Self:
        """join query parm
        """
        exit_query = parse.parse_qs(self.parse_result.query)
        str_query = parse.urlencode({**exit_query, **query})
        self.parse_result._replace(query=str_query)
        return self

    def to_str_url(self):
        return parse.urlunparse(self.parse_result)

    def __str__(self):
        return self.parse_result.__str__()
