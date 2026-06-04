# AI_LOG — UVA 11417 GCD Test Cases 設計

## 我問 AI 什麼

「請幫我設計 UVA 11417 GCD 的至少 3 個 test case，包含至少 1 個 edge case。題目是計算 1 ≤ i < j ≤ n 範圍內所有 gcd(i, j) 的總和。」

## AI 給了什麼

AI 提出了以下 test case 框架：
- n=1 作為 edge case
- n=2 作為簡單情況
- n=10 作為題目範例

## 我改了什麼

我根據題目邏輯驗證了各個 case 的預期輸出：

1. **n=1 (Edge Case)**：沒有 i < j 的組合存在，所以結果應為 0（不是任意數字，必須是 0）

2. **n=2 (Simple Case)**：只有一對 (1,2)，gcd(1,2)=1，總和=1（驗證基本邏輯）

3. **n=10 (General Case)**：選用題目官方範例答案 67，確保 test case 正確性

特別確認：
- 題目要求 **1 ≤ i < j** 而不是 **1 ≤ i ≤ j**，所以 edge case 必須是 n=1 的零和
- 三個 case 分別涵蓋最小值、簡單邏輯驗證、中等規模的完整測試

---

**下一步**：完成 gcd.py 實作，確保所有 test 從紅燈轉綠燈。
