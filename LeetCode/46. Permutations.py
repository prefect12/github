from itertools import permutations
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = list(permutations(nums))
        for i in range(len(n)):
            n[i] = list(n[i])
        return n