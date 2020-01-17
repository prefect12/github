class Solution:

    def searchRange(self, nums, target):
        right = n = len(nums) - 1
        left = 0

        if target not in nums or nums[n] < target or nums[0] > target:
            return [-1, -1]

        index_left = index_right = self.binary_search(left, right, target, nums)

        if index_left == -1:
            return [-1, -1]

        if index_left != 0:
            while index_left - 1 >= 0 and nums[index_left - 1] == target:
                index_left -= 1

        if index_right != n:
            while index_right + 1 <= n and nums[index_right + 1] == target:
                index_right += 1

        return [index_left, index_right]

    def binary_search(self, left, right, target, alist):
        mid = (left + right) // 2

        while alist[mid] != target:

            mid = (left + right) // 2

            if target < alist[mid]:
                right = mid - 1
            elif target > alist[mid]:
                left = mid + 1

            if left == right and alist[left] != target:
                return -1

        return mid


