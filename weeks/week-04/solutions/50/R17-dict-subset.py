# R17. 字典子集（1.17）

# 原始字典：key 是股票代號，value 是股價。
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# p1：用「值（value）」來過濾，保留股價大於 200 的項目。
# 字典推導式語法：{新key: 新value for ... if 條件}
# prices.items() 會逐筆提供 (key, value) 供我們檢查。
p1 = {k: v for k, v in prices.items() if v > 200}
print(p1)

# 先準備要保留的 key 集合（set）。
# 使用 set 做成員測試（k in tech_names）通常效率較好。
tech_names = {'AAPL', 'IBM'}

# p2：用「鍵（key）」來過濾，只留下指定名稱的股票。
# 這種寫法常用在「白名單篩選」情境：
# 例如只保留特定欄位、指定使用者、允許的設定鍵等。
p2 = {k: v for k, v in prices.items() if k in tech_names}
print(p2)