'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


'''


class Solution1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return (self.aux_uni([1, 1], [m, n], 0))

    def aux_uni(self, cur, final, num):
        if cur == final:
            return num + 1
        elif cur[0] < final[0] and cur[1] == final[1]:
            cur[0] += 1
            num = self.aux_uni(cur, final, num)
            cur[0] -= 1
        elif cur[1] < final[1] and cur[0] == final[0]:
            cur[1] += 1
            num = self.aux_uni(cur, final, num)
            cur[1] -= 1
        elif cur[0] < final[0] and cur[1] < final[1]:
            cur[0] += 1
            num = self.aux_uni(cur, final, num)
            cur[0] -= 1
            cur[1] += 1
            num = self.aux_uni(cur, final, num)
            cur[1] -= 1
        return num


#-----------------------------------------------------------------------------
def print_pretty(alist):
    for i in alist:
        for j in i:
            print(j,end='')
        print('\n')

class Solution2:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not i:
                    dp[i][j]=1
                elif not j:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                print_pretty(dp)
        return dp[m-1][n-1]

n = Solution2()
print(n.uniquePaths(2,3))
