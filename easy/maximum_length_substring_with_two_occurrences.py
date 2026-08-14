class Solution(object):
    def maximumLengthSubstring(self, s):
        left = 0
        counts = {}
        max_length = 0
        for right, character in enumerate(s):
            counts[character] = counts.get(character, 0) + 1

            while counts[character] > 2:
                left_character = s[left]
                counts[left_character] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


solution = Solution()
print(solution.maximumLengthSubstring("bcbbbcba"))
    

