class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        result = []
 
        for i in range(min(nums), max(nums) + 1):
            if i not in s:
                result.append(i)

                i += 1
        return result