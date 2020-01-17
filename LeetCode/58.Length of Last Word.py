class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = s.split()
        if n:
            if n[-1]:
                return len(n[-1])
        return 0
