import unicodedata


####################################################################################################
# 文字列操作に関するもの

class StrUtil:
    """文字列に関するユーティリティ
    """

    @staticmethod
    def full_width_char_count(value) -> int:
        """全角文字の数を数える.
        text    :対象の文字列
        """
        # 初期か
        count = 0
        # 文字を取り出す
        for char in value.__str__():
            # 全角の場合countに1足す
            if unicodedata.east_asian_width(char) in "FWA":
                count += 1

        return count

    @staticmethod
    def str_width(value: str) -> int:
        """半角文字を1、全角文字を2としたマジ幅を出力.
        """
        # 文字数 + 全角文字の数
        return len(value) + StrUtil.full_width_char_count(value)

    @staticmethod
    def add_comma(value: any):
        """カンマ付き文字列に変換する."""
        # 型の変換
        value = str(value)
        # フォーマット
        return f"{value:,}"

    @staticmethod
    def join_str(*values: any, sep: any = ""):
        """オブジェクトを連結した文字列を作成します.
        :param  any values :連結するオブジェクト
        :param  any sep    :連結するオブジェクトの間に挿入されるオブジェクト
        """
        # 連結する文字列がない場合空文字を返します
        if len(values) == 0:
            return ""

        # 最初の文字列で変数を初期化
        result = str(values[0])
        # 2つ目以降の文字列を取り出す
        for i in range(1, len(values)):
            # resultにsepと取り出した文字列を追加する
            result += str(sep) + str(values[i])

        # 連結した文字列を返す
        return result

    @staticmethod
    def split_by_limit(string: str, limit: int) -> list[str]:
        """最大文字幅に入るように複数の文字列に分割します
        """
        result = list[str]()
        line = ""

        while True:
            if StrUtil.str_width(string) <= limit:
                result.append(string)
                return result

            for char in string:
                if StrUtil.str_width(line) + StrUtil.str_width(char) > limit:
                    result.append(line)
                    string = string[len(line):]
                    line = ""
                    break
                line += char
