# U10. zip 為何只能用一次（1.8）

# 原始資料：股票代號對應價格
prices = {'A': 2.0, 'B': 1.0}

# zip(prices.values(), prices.keys()) 會把兩個可迭代物件逐項配對，
# 產生形如 (price, name) 的資料流：例如 (2.0, 'A'), (1.0, 'B')。
#
# 關鍵：zip 回傳的是「迭代器（iterator）」，不是 list。
# 迭代器是一次性資料流，元素被讀取後就不會自動回來。
z = zip(prices.values(), prices.keys())

# 第一次用 min(z) 時會把 z 走完（消耗掉）。
print(min(z))  # OK（消耗掉迭代器）

# 第二次再用 max(z) 時，z 已經是空的，
# 因此會出現：ValueError: max() arg is an empty sequence
print(max(z))  # 會失敗：因為 z 已經被消耗完

# 若需要重複使用，常見做法有兩種：
# 1) 先具體化：pairs = list(zip(...))，之後可多次 min/max。
# 2) 每次都重新建立 zip(...)，避免重用已消耗的迭代器。
