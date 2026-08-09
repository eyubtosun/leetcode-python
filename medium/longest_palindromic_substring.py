class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1] and len(piece) > len(longest):
                    longest = piece

        return longest


solution = Solution()
print(solution.longestPalindrome("babad"))
