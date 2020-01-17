'''
118. Pascal's Triangle
Easy
515
59


Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        alist = [[1] * (_ + 1) for _ in range(numRows)]

        for index1 in range(numRows):
            for j in range(1,index1):
                    alist[index1][j] = alist[index1-1][j] + alist[index1-1][j-1]

        return alist

#-----------------------------------------------
class Solution2:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        alist = [[0] * (_ + 1) for _ in range(numRows)]
        alist[0][0] = 1
        for index1, row in enumerate(alist):

            for i, num in enumerate(row):

                if i == 0 or i == len(row) - 1:
                    row[i] = 1

                elif num == 0:
                    row[i] = alist[index1 - 1][i - 1] + alist[index1 - 1][i]

        return alist


a = Solution()
print(a.generate(5))