class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            total = 1

            for digit in str(n):
                total *= int(digit)

            if total % t == 0:
                return n

            n += 1

solution = Solution()
print(solution.smallestNumber(2, 10))
