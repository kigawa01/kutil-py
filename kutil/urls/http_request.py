from urllib import request

from kutil.kutil.urls.url import URL


####################################################################################################
# httpリクエストに関するもの
class HttpRequest:
    """httpリクエストの情報を扱うクラス
    :var _url_request: リクエストの情報
    """
    _url_request: request.Request

    def __init__(self, url_request: request.Request):
        self._url_request = url_request

    @staticmethod
    def by_url(url: URL):
        """指定されたurlからHttpRequestを作成します
        """
        return HttpRequest(request.Request(url.to_str_url()))

    def get_request(self) -> request.Request:
        """現在のリクエストを取得します
        """
        return self._url_request
