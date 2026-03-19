# R19. 轉換+聚合：生成器表達式（1.19）

# 原始數列
nums = [1, 2, 3]

# 生成器表達式 + sum：
# 先把每個 x 轉成 x*x（平方），再由 sum 做加總。
# 寫成生成器可避免先建立中間 list，較省記憶體。
print(sum(x * x for x in nums))

# tuple 資料，可能是混合型別（字串、整數、浮點數）
s = ('ACME', 50, 123.45)

# 生成器表達式 + join：
# join 只能串接字串，因此先用 str(x) 逐筆轉型，
# 再以逗號把所有欄位串成一行文字。
print(', '.join(str(x) for x in s))

# 由多個 dict 組成的投資組合資料
portfolio = [{'name': 'AOL', 'shares': 20}, 
             {'name': 'YHOO', 'shares': 75}]

# 用生成器先取出每筆 shares，再找最小值（只回傳最小數字）。
print(min(s['shares'] for s in portfolio))

# 直接對整個資料列做 min，搭配 key 指定比較欄位。
# 這行會回傳「整筆 dict」，而不是單一 shares 數值。
print(min(portfolio, key=lambda s: s['shares']))
