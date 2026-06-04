def count_squares(a, b):
    """計算 [a, b] 區間內完全平方數的個數
    
    若 a > b，raise ValueError。
    """
    if a > b:
        raise ValueError("a must be <= b")
    
    count = 0
    i = 1
    while i * i <= b:
        if i * i >= a:
            count += 1
        i += 1
    
    return count
