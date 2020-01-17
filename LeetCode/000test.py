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
                j += 1
                num += 1
            j -= 1
            i += 1

            while i < n:
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = num
                i += 1
                num += 1
            i -= 1
            j -= 1

            while j >= 0 :
                if matrix[i][j] != 0:
                    break
                matrix[i][j] = num
                j -= 1
                num += 1
            j += 1
            i -= 1

            while i >= 0 :
                if matrix[i][j] != 0:
                    j+=2
                    break
                matrix[i][j] = num
                i -= 1
                num += 1
            i += 1
            j -= 1

        return matrix

if __name__ == "__main__":
    solution = Solution()
    a = solution.generateMatrix(0)
    for i in a:
        print(i)
