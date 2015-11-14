#!/usr/bin/python3
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, x in enumerate(nums):
            try:
                return seen[x] + 1, i + 1
            except KeyError:
                seen.setdefault(target - x, i)
