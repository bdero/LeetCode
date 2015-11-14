import unittest
from problems import two_sum, three_sum


class GenericSolutionTest(unittest.TestCase):
    def setUp(self):
        if not hasattr(self, 'module'):
            raise AttributeError(
                'The `module` property must be defined in all subclasses of '
                'GenericSolutionTest'
            )
        self.solution = self.module.Solution()


class TwoSum(GenericSolutionTest):
    module = two_sum

    def test_two_sum(self):
        self.assertTupleEqual(
            self.solution.twoSum([2, 7, 11, 15], 9),
            (1, 2)
        )
        self.assertTupleEqual(
            self.solution.twoSum([3, 2, 4], 6),
            (2, 3)
        )


class ThreeSum(GenericSolutionTest):
    module = three_sum

    def test_empty(self):
        self.assertListEqual(self.solution.threeSum(None), [])

    def test_simple(self):
        self.assertListEqual(
            self.solution.threeSum([-1, 0, 1, 2, -1, -4]),
            [(-1, -1, 2), (-1, 0, 1)]
        )


if __name__ == '__main__':
    unittest.main()
