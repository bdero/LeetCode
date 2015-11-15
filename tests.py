import unittest
from problems import two_sum, three_sum, add_two_numbers


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


class AddTwoNumbers(GenericSolutionTest):
    module = add_two_numbers

    def setUp(self):
        super(AddTwoNumbers, self).setUp()
        self.ListNode = self.solution.ListNode

    def test_carry(self):
        l1 = self.ListNode(1)
        l1.next = self.ListNode(2)
        l1.next.next = self.ListNode(3)
        l2 = self.ListNode(1)
        l2.next = self.ListNode(9)
        l2.next.next = self.ListNode(2)

        result = self.solution.addTwoNumbers(l1, l2)

        self.assertListEqual(list(result), [2, 1, 6])


if __name__ == '__main__':
    unittest.main()
