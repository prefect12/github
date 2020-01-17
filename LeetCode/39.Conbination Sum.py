'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''

#solution 1
import itertools
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        new_list = []
        for m in range(1,target//min(candidates)+1):
            n = itertools.combinations_with_replacement(candidates,m)
            for i in n:
                if sum(i) == target:
                    new_list.append(list(i))
        return new_list


def combination(candidates,target):
    res = []
    return aux_combination(candidates,target,[],res)

def aux_combination(candidates,target,cur,res):
    if cur < 0:
        return
    if cur == 0:
        res.append([cur])
        return
    for i in range(len(candidates)):
        aux_combination(candidates[i:],target - candidates[i],cur+[candidates[i]],res)


#solution 2\

class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates, target, [], res)
        return res

    def helper(self, candi, target, cur, res):
        if target < 0:
            return
        if target == 0:
            res.append(cur)
            return
        for i in range(len(candi)):
            self.helper(candi[i:], target - candi[i], cur + [candi[i]], res)

n = Solution2()
print(n.combinationSum([10,1,2,7,6,1,5],8))
            
