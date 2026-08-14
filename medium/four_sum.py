class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        quadruplets = []

        for first in range(len(nums) - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, len(nums) - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                left = second + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[first] + nums[second] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        quadruplets.append(
                            [nums[first], nums[second], nums[left], nums[right]]
                        )
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return quadruplets
