class Solution(object):
    def lengthOfLongestSubstring(self, s):
        current = ""
        longest = 0
        for letter in s:
            if letter not in current:
                current += letter
            else:
                current = current[current.index(letter) + 1:] + letter

            longest = max(longest, len(current))
        
        return longest
    


