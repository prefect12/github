'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''
import itertools
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [list(a) for a in itertools.combinations(list(range(1,n+1)),k)]

    def combine1(n,k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in combine(i - 1, k - 1)]

    def combine2(self, n, k):
        if k == 0:
            return [[]]

        return list(itertools.combinations(list(range(1, n + 1)), k))

if __name__ == "__main__":
    print(combine(4,2))