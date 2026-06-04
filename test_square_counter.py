"""平方數計數 — 測試檔案

題目：count_squares(a, b) 回傳 [a, b] 區間內完全平方數的個數。
      若 a > b，應 raise ValueError("a must be <= b")。

Test Cases（跟 AI 討論後完善）：
  1. test_basic_range: count_squares(1, 10) = 3（1, 4, 9）
  2. test_single_point_is_square: count_squares(4, 4) = 1（單點，是平方數）
  3. test_no_squares_in_range: count_squares(2, 3) = 0（區間無平方數）
  4. test_invalid_input_raises: count_squares(5, 2) → ValueError

AI 提示：確認平方數的邏輯，驗證例外處理。
"""

import unittest

# from square_counter import count_squares  # 完成後解除註解


class TestCountSquares(unittest.TestCase):
    def test_basic_range(self):
        """基本情況：[1, 10] 含有 3 個平方數 (1, 4, 9)"""
        self.assertEqual(count_squares(1, 10), 3)

    def test_single_point_is_square(self):
        """Edge case：單點區間，且是平方數 (4 = 2²)"""
        self.assertEqual(count_squares(4, 4), 1)

    def test_no_squares_in_range(self):
        """Edge case：區間內沒有任何平方數"""
        # 1² = 1 < 2, 2² = 4 > 3
        self.assertEqual(count_squares(2, 3), 0)

    def test_invalid_input_raises(self):
        """例外情況：a > b 應 raise ValueError"""
        with self.assertRaises(ValueError):
            count_squares(5, 2)


if __name__ == "__main__":
    unittest.main()
