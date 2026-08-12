

class Solution:
    def hasDuplicate(self, nums):
        duplicate = []

        for number in nums:
            if number not in duplicate:
                duplicate.append(number)
            else:
                return True

        return False


solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))
