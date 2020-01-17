'''


'''


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    long_str = ''
    cur = ''
    for i in range(len(s)):
        if s[i] not in cur:
            cur += s[i]
        else:
            cur = cur[cur.index(s[i])+1:] + s[i]
        long_str = max(long_str, cur, key=lambda x: len(x))
    return len(long_str)

#######################
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        long_str = 0
        cur = ''
        for i in range(len(s)):
            if s[i] not in cur:
                cur += s[i]
            else:
                cur = cur[cur.index(s[i]) + 1:] + s[i]
            long_str = max(len(cur),long_str)

        return long_str
