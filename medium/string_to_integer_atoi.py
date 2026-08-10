class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        sign = 1
        index = 0
        if not s:
            return 0
        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == "+":
            index += 1

        number = 0

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            number = number * 10 + digit
            index += 1

        number *= sign

        minimum = -(2**31)
        maximum = 2**31 - 1

        if number < minimum:
            return minimum

        if number > maximum:
            return maximum

        return number


solution = Solution()
print(solution.myAtoi("42"))

