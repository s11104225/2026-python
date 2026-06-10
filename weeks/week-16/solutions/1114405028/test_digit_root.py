import unittest
from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(digit_root(9875), 2)

    def test_edge_case_large_multiple_of_9(self):
        self.assertEqual(digit_root(999999999), 9)

    def test_single_digit(self):
        self.assertEqual(digit_root(1), 1)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError):
            digit_root(0)
        with self.assertRaises(ValueError):
            digit_root(-5)
        with self.assertRaises(ValueError):
            digit_root(3.14)


if __name__ == "__main__":
    unittest.main()
