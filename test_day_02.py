import unittest
from day_02 import is_continuous, is_safe, is_ordered

class TestDay02(unittest.TestCase):
    def test_is_ordered(self):
        test_cases = [
            ([1, 2, 3, 4, 5], True, "Increasing sequence"),
            ([5, 4, 3, 2, 1], True, "Decreasing sequence"),
            ([1, 2, 2, 3], False, "Not strictly increasing"),
            ([3, 3, 2, 1], False, "Not strictly decreasing"),
            ([1, 3, 2, 4], False, "Neither increasing nor decreasing"),
            ([1], True, "Single element"),
            ([], True, "Empty list"),
            ([1, 1], False, "Two equal elements"),
            ([3, 2, 1, 2], False, "Changes direction"),
            ([5, 4, 3, 3], False, "Decreasing then equal")
        ]
        for numbers, expected, msg in test_cases:
            with self.subTest(msg=msg):
                self.assertEqual(is_ordered(numbers), expected)


    def test_is_continuous(self):
        test_cases = [
            ([1, 2, 3, 4], True, "Valid sequence 1"),
            ([4, 3, 2, 1], True, "Valid sequence 1"),
            ([2, 4, 5, 7], True, "Valid sequence 2"),
            ([1, 2, 6, 7], False, "Gap too large 1"),
            ([1, 5, 6, 7], False, "Gap too large 2"),
            ([1], True, "Single element"),
            ([], True, "Empty list")
        ]
        for numbers, expected, msg in test_cases:
            with self.subTest(msg=msg):
                self.assertEqual(is_continuous(numbers), expected)

    def test_is_safe(self):
        test_cases = [
            ([7, 6, 4, 2, 1], True, "Safe without removing any level 1"),
            ([1, 2, 7, 8, 9], False, "Unsafe regardless of which level is removed"),
            ([9, 7, 6, 2, 1], False, "Unsafe regardless of which level is removed"),
            ([1, 3, 2, 4, 5], True, "Safe by removing 3"),
            ([8, 6, 4, 4, 1], True, "Safe by removing one 4"),
            ([54, 57, 58, 60, 66], True, "Safe as removing the large gap"),
            ([1, 3, 6, 7, 9], True, "Safe without removing any level"),
            ([25, 20, 19, 19, 18, 19], False, "Unsafe removing a level 1"),
            ([19, 18, 19, 19, 20, 25], False, "Unsafe removing a level 2"),
        ]
        for numbers, expected, msg in test_cases:
            with self.subTest(msg=msg):
                self.assertEqual(is_safe(numbers), expected)

if __name__ == '__main__':
    unittest.main()