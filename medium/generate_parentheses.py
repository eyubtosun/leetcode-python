"""Generate all combinations of well-formed parentheses."""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, opened, closed):
            if len(current) == n * 2:
                result.append(current)
                return

            if opened < n:
                backtrack(current + "(", opened + 1, closed)

            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return result


solution = Solution()
print(solution.generateParenthesis(3))
