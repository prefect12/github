'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
import itertools


class Solution:
    def subsets(self, nums):
        result = []

        if nums:
            for i in range(len(nums) + 1):
                for m in itertools.combinations(nums, i):
                    result.append(list(m))
            return result
        else:
            return nums