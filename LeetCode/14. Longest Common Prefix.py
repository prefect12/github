'''
14. Longest Common Prefix
Easy

1836

1580

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''


class Solution1:
    def longestCommonPrefix(self, strs):
        min_len = min([len(x) for x in strs])
        result = ''

        for i in range(1,min_len+1):
            prefix = strs[0][:i]
            for s in strs:
                if s[:i] != prefix:
                    return result
            result = prefix

        return result

class Solution2:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            print(i,letter_group)
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

if __name__ == "__main__":
    alist = ['abc', 'abd', 'abcdefg']
    solution = Solution2()
    result = solution.longestCommonPrefix(alist)
    print(result)
