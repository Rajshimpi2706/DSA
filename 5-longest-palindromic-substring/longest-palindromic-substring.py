class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        longest = ""
        def expand_centre(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        for i in range(len(s)):
            odd = expand_centre(i, i)
            even = expand_centre(i, i+1)
            if len(odd) > len(longest):
                longest = odd

            if len(even) > len(longest):
                longest = even

        return longest
        """
        :type s: str
        :rtype: str
        """
        