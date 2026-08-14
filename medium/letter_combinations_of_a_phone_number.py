class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        combinations = [""]
        for digit in digits:
            next_combinations = []
            for combination in combinations:
                for letter in phone[digit]:
                    next_combinations.append(combination + letter)
            combinations = next_combinations

        return combinations
    
solution = Solution()
print(solution.letterCombinations("23"))