# AI_LOG — count_squares Test Cases 設計

## 我問 AI 什麼

「請幫我設計平方數計數功能的至少 3 個 test case，包含 edge case 和例外情況。題目是 count_squares(a, b) 計算 [a, b] 區間內的完全平方數個數，若 a > b 應 raise ValueError。」

## AI 給了什麼

AI 提出了以下 test case 框架：
- count_squares(1, 10)：基本情況
- 單點區間的 edge case
- 無平方數的 edge case
- a > b 的 ValueError 案例

## 我改了什麼

我根據題目邏輯驗證並完善了各個 case 的預期輸出：

1. **test_basic_range**: count_squares(1, 10) = 3
   - 驗證：1² = 1, 2² = 4, 3² = 9 ✓ （4² = 16 > 10）
   - 測試基本邏輯

2. **test_single_point_is_square**: count_squares(4, 4) = 1
   - Edge case：單點區間 (a == b) 且是完全平方數
   - 4 = 2²，所以結果是 1 ✓
   - 測試邊界條件

3. **test_no_squares_in_range**: count_squares(2, 3) = 0
   - Edge case：區間長度 > 1 但無平方數
   - 1² = 1 < 2, 2² = 4 > 3，結果是 0 ✓
   - 測試空集合情況

4. **test_invalid_input_raises**: count_squares(5, 2)
   - 例外情況：a > b 必須 raise ValueError ✓
   - 使用 assertRaises 驗證

特別確認：
- 題目明確要求 a > b 時的例外處理
- Edge case 必須涵蓋單點、無結果等邊界
- 所有 case 都使用整數，符合題目要求

---

**下一步**：完成 square_counter.py 實作，確保所有 test 從紅燈轉綠燈。
