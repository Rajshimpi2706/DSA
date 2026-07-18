class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        merge = []
        while i < m and j < n:

            if nums1[i] <= nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1

        while i < m:
            merge.append(nums1[i])
            i += 1

        while j < n:
            merge.append(nums2[j])
            j += 1

        # Copy merged array back into nums1
        for k in range(m + n):
            nums1[k] = merge[k]
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        