"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]
 

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List, Tuple


class Solution:
    """For-Loop is hard-coded, but it works."""
    def __init__(self):
        self.phone_dict = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        if len(digits) == 4:
            for i in self.phone_dict[digits[0]]:
                for j in self.phone_dict[digits[1]]:
                    for k in self.phone_dict[digits[2]]:
                        for l in self.phone_dict[digits[3]]:
                            results.append(i + j + k + l)

        elif len(digits) == 3:
            for i in self.phone_dict[digits[0]]:
                for j in self.phone_dict[digits[1]]:
                    for k in self.phone_dict[digits[2]]:
                            results.append(i + j + k)

        elif len(digits) == 2:
            for i in self.phone_dict[digits[0]]:
                for j in self.phone_dict[digits[1]]:
                    results.append(i + j)

        elif len(digits) == 1: 
            return self.phone_dict[digits]


        elif len(digits) == 0:
            return results


        return results


from itertools import product
class Solution: 
    """Same working solution but cleaner Python code."""
    def __init__(self):
        self.phone_dict = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letter_groups = [self.phone_dict[d] for d in digits]
        return [''.join(combo) for combo in product(*letter_groups)]


test_cases = [
    ("", []),
    ("2", ["a", "b", "c"]),
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("7", ["p", "q", "r", "s"]),
    ("92", ["wa", "wb", "wc", "xa", "xb", "xc", "ya", "yb", "yc", "za", "zb", "zc"]),
]

def normalized_test_cases(cases):
    return [(digits, sorted(output)) for digits, output in cases]

run_test_cases(
    func=lambda digits: sorted(Solution().letterCombinations(digits)),
    test_cases=normalized_test_cases(test_cases),
    description="Letter Combinations of a Phone Number"
)
