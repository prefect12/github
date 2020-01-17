'''
59. Spiral Matrix II
Medium

713

96

Add to List

Share
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        i = j = 0
        num = 1

        while num <= n * n:
            while j < n :
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = num
                j,num = j+1,num+1
            j,i = j-1,i+1

            while i < n:
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = num
                i,num = i+1,num+1
            i,j =i-1,j-1

            while j >= 0 :
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = num
                j,num = j-1,num+1
            j,i = j+1,i-1

            while i >= 0 :
                if matrix[i][j] != 0:
                    j+=2
                    break
                matrix[i][j] = num
                i,num = i-1,num+1
            i,j = i+1,j-1


        return matrix