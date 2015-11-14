#!/usr/bin/python3
# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        nums = sorted(nums)

        tail = lambda l: ((l[n], l[n + 1:]) for n in range(len(l) - 1))

        a_last = None
        for a, a_tail in tail(nums):
            if a_last == a:
                continue
            a_last = a

            b_last = None
            for b, b_tail in tail(a_tail):
                if b_last == b:
                    continue
                b_last = b

                if -(a + b) in b_tail:
                    result.append((a, b, -(a + b)))

        return result
