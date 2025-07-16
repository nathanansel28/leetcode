from typing import List, Tuple
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG = True
logger = load_logger(DEBUG)


class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            return (
                self.isMatch(text, pattern[2:])
                or first_match
                and self.isMatch(text[1:], pattern)
            )
        else:
            return first_match and self.isMatch(text[1:], pattern[1:]) 

    def match(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], "."}
        return first_match and self.match(s[1:], p[1:])