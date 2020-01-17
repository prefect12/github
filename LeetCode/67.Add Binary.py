'''

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


'''

from itertools import zip_longest


class Solution:

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list = list(a)
        b_list = list(b)
        c = ''
        care = 0
        for a, b in zip_longest(a_list[::-1], b_list[::-1], fillvalue='0'):
            num = (int(a) + int(b) + care) % 2
            care = (int(a) + int(b) + care) // 2
            c = str(num) + c
        if care != 0:
            c = str(care) + c
        return c