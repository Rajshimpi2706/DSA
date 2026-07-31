class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
    

        stack = []
        next_greater = {}

        # Find next greater element for every number in nums2
        for num in nums2:

            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)

        # Remaining elements have no next greater element
        while stack:
            next_greater[stack.pop()] = -1

        result = []

        # Build answer for nums1
        for num in nums1:
            result.append(next_greater[num])

        return result
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        