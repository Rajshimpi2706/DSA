class Solution(object):
    def removeDuplicates(self, num):
        if len(num) == 0:
            return 0
        left = 0

        for right in range(len(num)):
            if num[left] != num[right]:
                left += 1
                num[left] = num[right]
        return left + 1


        """
        :type nums: List[int]
        :rtype: int
        """
        