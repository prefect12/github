'''


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


'''

#Solution 1 three
class Solution:

    def __init__(self):
        self.answer = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.aux_generate(n,n,'')
        return self.answer

    def aux_generate(self,left,right,current):

        if right < left:
            return

        if not left and not right:
            self.answer.append(current)

        if left > 0:
            self.aux_generate(left-1,right,current+'(')

        if right > 0:
            self.aux_generate(left,right-1,current+')')

if __name__=="__main__":
    N = Solution()
    alist = N.generateParenthesis(3)
    print(alist)


