"""UVA 11417 GCD — 測試檔案

題目：sum_of_gcd(n) 計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。

Test Cases（跟 AI 討論後完善）：
  1. test_edge_case_n_equals_1: n=1，無組合，總和=0
  2. test_n_equals_2: n=2，只有 gcd(1,2)=1，總和=1
  3. test_n_equals_10: n=10，題目範例答案=67

AI 提示：先確認算法邏輯，驗證 gcd 計算無誤。
"""

import unittest

# from gcd import sum_of_gcd  # 完成 gcd.py 後解除註解


class TestSumOfGcd(unittest.TestCase):
    def test_edge_case_n_equals_1(self):
        """Edge case: n=1，沒有 i < j 的組合"""
        # 當 n=1 時，無法有 i < j，所以總和應為 0
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_2(self):
        """Simple case: n=2，只有一對 (1,2)"""
        # gcd(1,2) = 1
        # 總和 = 1
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_10(self):
        """General case: n=10，題目範例"""
        # 根據 UVA 11417，n=10 的答案是 67
        self.assertEqual(sum_of_gcd(10), 67)


if __name__ == "__main__":
    unittest.main()
