'''

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        return self.aux_combi(candidates,target,res,[],0)
    def aux_combi(self,candi,target,res,cur,ind):
        if target == 0:
            n = sorted(cur)
            if n not in res:
                res.append(n)
        if target < 0:
            return
        for i in range(ind,len(candi)):
            self.aux_combi(candi,target-candi[i],res,cur+[candi[i]],i+1)
        return res