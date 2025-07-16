"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]
 

Constraints:
    1 <= n <= 8
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List, Tuple, Optional

class Checker: 
    """Works but not optimized."""
    def __init__(self):
        self.start = [
            "(", "[", "{"
        ]
        self.end = [
            ")", "]", "}"
        ]

    def map(self, s: str) -> str: 
        return s.replace(
            "{", "}" 
        ).replace(
            "(", ")"
        ).replace(
            "[", "]"
        ) 

    def isValid(self, s: str) -> bool: 
        if len(s) % 2 != 0:
            return False
        
        q = []
        for char in s:
            if char in self.start: 
                q.append(char) 
            elif char in self.end:
                if len(q) == 0:
                    return False
                check = q.pop()
                logger.debug(f"char: {char} | check: {check}")
                if char != self.map(check):
                    return False

        return True if len(q) == 0 else False


class Solution:
    def __init__(self):
        self.checker = Checker()
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        
        for _ in range(n):
            results.append()



def permutate(output: List):
    from itertools import permutations
    normalized = [tuple(sorted(triplet)) for triplet in output]    
    perms = set(permutations(normalized))
    return [ [list(t) for t in perm] for perm in perms ]

test_cases = [
    (3, ["((()))","(()())","(())()","()(())","()()()"]), 
    (1, ["()"])
]
test_cases = [(input, permutate(output)) for input, output in test_cases]

run_test_cases(Solution().generateParenthesis, test_cases)
