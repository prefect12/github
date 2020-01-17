class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return
        temp = nums1[:m]
        a = b = 0
        for i in range(m+n):
            if a == m:
                nums1[:] = nums1[:i] + nums2[b:]
                break
            elif b == n:
                nums1[:] = nums1[:i] + temp[a:]
                break
            if temp[a] <= nums2[b]:
                nums1[i] = temp[a]
                a += 1
            elif temp[a] > nums2[b]:
                nums1[i] = nums2[b]
                b += 1
if __name__ == "__main__":
    solution = Solution()
    a = solution.merge([1,2,3,0,0,0],3,[2,5,6],3)
    print(a)