"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        left = s[:len(s)//2]
        right = s[len(s)//2:]
        right = right.replace(
            "}", "{"
        ).replace(
            ")", "("
        ).replace(
            "]", "["
        )
        logger.debug(f"left: {left}")
        logger.debug(f"right: {right[::-1]}")
        return left == right[::-1]


class Solution: 
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


test_cases = [
    ("()", True), 
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("{[{]}}", False),
    ("((", False),
    ("){", False),
    ("{}}{}{}{}{}{}{}{}{}{}}", False),
    ("{({({({({({})})})})})}", True), 
    ("[(])", False)
]

run_test_cases(Solution().isValid, test_cases)
