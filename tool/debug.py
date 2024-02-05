
# utilities
####################################################################################################
# debug tools

# デバッグモードを有効にするフラグ
is_debug = False


def debug(*message: any):
    """デバッグモードが有効な場合にオブジェクトをプリントします.
    :var message    :プリントするオブジェクト
    """
    if is_debug:
        print("[debug]", *message)
