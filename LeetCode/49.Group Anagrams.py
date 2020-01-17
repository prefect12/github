'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''


class Solution1:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = [[] for i in range(len(strs))]
        newlist = []
        for i in strs:
            if set(i) not in newlist:
                m = sorted(tuple(i))
                newlist.append(m)
            output[newlist.index(m)].append(i)
        return [n for n in output if n]

#-----------------------------------------------------------
class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a_dic = {}
        for i in strs:
            m = tuple(sorted(i))
#----------------------------------
            if m not in a_dic:
                a_dic[m] = []
            a_dic[m].append(i)
#can be replaced by:
            #a_dic[m] = a_dic.get(m,[]) + [i]
# ----------------------------------
        return list(a_dic.values())