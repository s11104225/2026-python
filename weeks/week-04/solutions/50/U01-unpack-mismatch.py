# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

p = (4, 5)
# x, y, z = p  # ValueError：元素只有 2 個但變數要 3 個
print(p)

x, y= p  # 正確：變數數量與元素數量相同
print(x, y)