# R18. namedtuple（1.18）

# 從 collections 匯入 namedtuple 工廠函式。
# namedtuple 可以建立「具名欄位」的 tuple 類別，
# 兼具 tuple 的輕量特性與可讀性更高的屬性存取方式。
from collections import namedtuple

# 定義一個名為 Subscriber 的具名 tuple 類別，
# 欄位依序為 email（信箱）與 joined（加入日期）。
Subscriber = namedtuple('Subscriber', ['email', 'joined'])

# 建立 Subscriber 實例。
# 雖然底層是 tuple，但可用屬性名稱存取欄位。
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
# 以屬性名稱讀取資料，比起 sub[0] 更直觀。
sub.email
print(sub.email)
# 再建立一個 Stock 類別，表示股票資料：名稱、股數、單價。
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)

# namedtuple 是不可變（immutable）結構，不能直接改 s.shares。
# _replace(...) 會回傳「新的」Stock 實例，並套用指定欄位變更。
# 這裡把 shares 從 100 更新為 75。
s = s._replace(shares=75)
print(s)

class StockClass:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def _replace(self, **kwargs):
        # 傳統類別的 _replace 實作：建立新實例並套用變更。
        # if kwargs 中的 key 不存在於 self.__dict__，會直接新增屬性，
        # 而不是像 namedtuple 那樣限制只能替換既有欄位
        params = {**self.__dict__, **kwargs}
        return StockClass(**params)

# 傳統類別的實例，屬性可變。
s2 = StockClass('ACME', 100, 123.45)
print(s2.name, s2.shares, s2.price)