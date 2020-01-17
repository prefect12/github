from itertools import permutations
class Solution:
    def permuteUnique(self,nums):
        new_list = []
        a = permutations(nums)
        for i in a:
            if list(i) not in new_list:
                new_list.append(list(i))
        print(new_list)

    def permuteUnique2(self, nums):
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in range((p + [n]).index(n) + 1)]
        return perms

if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique2([1,2,3]))