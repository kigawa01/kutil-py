import hashlib


class Hash:
    """hashを扱うクラス
    """

    @staticmethod
    def hash(value: any) -> str:
        """hashを行う
        """
        return hashlib.sha512(str(value).encode("utf-8")).hexdigest()
