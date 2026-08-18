class Solution(object):
    def removeElement(self, nums, val):
        write = 0
        for number in nums:
            if number != val:
                nums[write] = number
                write += 1

        return write


solution = Solution()
print(solution.removeElement([1, 7, 5, 7], 7))
