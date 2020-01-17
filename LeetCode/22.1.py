class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):

        alist = self.aux_generateParenthesis(n, n, [], "")
        return alist

    def aux_generateParenthesis(self, left, right, alist, current):
        if right < left:
            return alist

        if left == right == 0:
            alist.append(current)
            return alist

        if left != 0:
            alist = self.aux_generateParenthesis(left - 1, right, alist, current + "(")

        if right != 0:
            alist = self.aux_generateParenthesis(left, right - 1, alist, current + ")")

        return alist

if __name__ == "__main__":
    solution = Solution()
    alist = solution.generateParenthesis(3)
    print(alist)