import unittest
from two_sum import Solution

class two_sum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_something(self):
        self.assertTupleEqual(
            self.solution.twoSum([2, 7, 11, 15], 9),
            (1, 2)
        )
        self.assertTupleEqual(
            self.solution.twoSum([3, 2, 4], 6),
            (2, 3)
        )


if __name__ == '__main__':
    unittest.main()
