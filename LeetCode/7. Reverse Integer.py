'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = abs(x)
        string = str(n)
        string = string[-1::-1]
        if int(string) not in range(2**31-1):
            return 0
        if x < 0:
            return -int(string)
        else:
            return int(string)