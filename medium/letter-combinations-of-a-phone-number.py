17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/


_KEYPAD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        combinations = [""]
        
        for digit in digits:
            possible_letters = _KEYPAD[digit]
            new_combinations = []
            for letter in possible_letters:
                for combination in combinations:
                    new_combinations.append(combination + letter)
            
            combinations = new_combinations
        
        return combinations
        