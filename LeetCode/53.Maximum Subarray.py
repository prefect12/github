'''

#Kadane's Algorithm

'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = n = nums[0]
        for num in nums[1:]:
            m = max(m + num, num)
            n = max(m, n)
        return n

if __name__ == "__main__":
    n = Solution()
    alist = [-3,1,2,3,4,-4,5,-1,-2,-5]
    m = n.maxSubArray(alist)
    print(m)