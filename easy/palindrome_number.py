class Solution(object):
    def isPalindrome(self, x):
        text = str(x)
        return text == text[::-1]


result = Solution().isPalindrome(121)
print(result)
