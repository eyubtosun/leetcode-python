class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        middle = length // 2
        if length % 2 == 1:
            return merged[middle]
        else:
            left_middle = merged[middle - 1]
            right_middle = merged[middle]
            return (left_middle + right_middle) / 2.0


solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))