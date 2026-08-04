class Solution(object):
    def maxProduct(self, n):

        first = 0
        second = 0

        for digit in str(n):
            digit = int(digit)
            if digit > first:
                second = first
                first = digit
            elif digit > second:
                second = digit
        return first * second