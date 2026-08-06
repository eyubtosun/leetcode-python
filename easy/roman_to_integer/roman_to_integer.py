# Roman to Integer


class Solution(object):
    def romanToInt(self, s):
        values = {
           "I":1,
           "V":5,
           "X":10,
           "L":50,
           "C":100,
           "D":500,
           "M":1000
        }

        total = 0

        for i in range(len(s)):
            current_value = values[s[i]]
            next_value = 0

            if i + 1 < len(s):
                next_value = values[s[i + 1]]

            if current_value < next_value:
                total -= current_value
            else:
                total += current_value

        return total


result = Solution().romanToInt("MCMXCIV")
print(result)
