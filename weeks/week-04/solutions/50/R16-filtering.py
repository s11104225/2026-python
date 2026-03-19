# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 原始整數資料，包含正數與負數。
mylist = [1, 4, -5, 10]

# 串列推導式：立即建立一個新的 list，留下大於 0 的元素。
# 特性：結果會一次建立完成，適合資料量不大且後續需要重複使用結果的情境。
[n for n in mylist if n > 0]

# 生成器運算式：建立一個 generator 物件，條件同樣是 n > 0。
# 特性：惰性計算（lazy evaluation），只有在迭代時才逐筆產生元素，
# 較節省記憶體，適合大型資料流。
pos = (n for n in mylist if n > 0)

# 混合字串資料，包含可轉整數與不可轉整數的值。
values = ['1', '2', '-3', '-', 'N/A']

# 自訂判斷函式：檢查字串是否可安全轉成整數。
# 可轉成功回傳 True；轉換失敗（ValueError）回傳 False。
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# filter(function, iterable)：保留 function(item) 為 True 的項目。
# 這裡會篩出可轉成整數的字串，最後再用 list(...) 具體化結果。
print(list(filter(is_int, values)))
#[n for n in values if is_int(n)] # <---

# compress(data, selectors)：依 selectors 的布林值篩選 data。
# selectors 與 data 會依索引位置一一對應。
from itertools import compress

# 待篩選資料（例如地址）
addresses = ['a1', 'a2', 'a3']

# 對應的數值（例如各地址統計數）
counts = [0, 3, 10]

# 先建立布林遮罩：只保留大於 5 的項目。
more5 = [n > 5 for n in counts]

# 根據 more5 的 True/False 過濾 addresses。
# counts 中只有 10 大於 5，所以結果會留下 'a3'。
print(list(compress(addresses, more5)))
