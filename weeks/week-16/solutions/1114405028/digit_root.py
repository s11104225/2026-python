def digit_root(n: int) -> int:
    """
    回傳 n 的數字根。若 n < 1 或 n 不是整數，raise ValueError("n must be >= 1")
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be >= 1")
    while n >= 10:
        s = 0
        while n:
            s += n % 10
            n //= 10
        n = s
    return n
