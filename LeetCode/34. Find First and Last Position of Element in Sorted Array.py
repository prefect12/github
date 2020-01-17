'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n, m = 0, len(nums) - 1
        finder = None

        while n <= m :
            mid = (m + n) // 2
            if target == nums[mid]:
                finder = mid
            if nums[mid] > target:
                m = mid-1
            elif nums[mid] <= target:
                n = mid+1
        if finder is None:
            return [-1,-1]
        new_list = [finder, finder]

        if new_list[0] != 0:
            while new_list[0] - 1 >= 0 and nums[new_list[0] - 1] == target:
                new_list[0] -= 1
        if new_list[1] != len(nums)-1:
            while  new_list[1] < len(nums) - 1 and nums[new_list[1] + 1] == target:
                new_list[1] += 1
        return new_list


a = Solution()
print(a.searchRange([1,2,2,3],3))