class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n = int(dividend / divisor)
        if n > 2 ** 31 - 1:
            n = 2147483647
        if n < -2 ** 31:
            n = -2147483648
        return n
