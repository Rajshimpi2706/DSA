class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combine = nums1 + nums2
        combine.sort()
        n = len(combine)
        if n % 2 != 0:
            return combine[n//2]
        else :
            mid1 = combine[(n//2) -1]
            mid2 = combine[n//2]
            return (mid1 + mid2)/2.0
        

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        