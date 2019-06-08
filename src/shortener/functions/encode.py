BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base_62_encode(id, alphabet=BASE62):
    """Encode a positive number in Base X

    Arguments:
    - `id`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if id == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while id:
        id, rem = divmod(id, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)
