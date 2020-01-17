'''
119. Pascal's Triangle II
Easy
361
139


Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

'''


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        rowIndex += 1
        alist = [[0] * (_ + 1) for _ in range(rowIndex)]
        alist[0][0] = 1
        for index1, row in enumerate(alist):

            for i, num in enumerate(row):

                if i == 0 or i == len(row) - 1:
                    row[i] = 1

                elif num == 0:
                    row[i] = alist[index1 - 1][i - 1] + alist[index1 - 1][i]

        return alist[-1]