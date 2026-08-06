class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for bracket in s:
            if bracket not in pairs:
                stack.append(bracket)
            else:
                if not stack:
                    return False

                if stack.pop() != pairs[bracket]:
                    return False

        return not stack

solution = Solution()
print(solution.isValid("())"))

#0ms run time
