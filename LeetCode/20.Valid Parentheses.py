class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stuck,dic = [],{'(': ')', '[': ']', '{': '}'}

        for i in range(len(s)):
            if s[i] in dic:
                stuck.append(dic[s[i]])
            else:
                if stuck == [] or s[i] != stuck.pop():
                    return False
        return not stuck
