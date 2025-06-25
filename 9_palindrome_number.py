from typing import List, Tuple
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG = True
logger = load_logger(DEBUG)

import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Solving without converting integer to string."""
        if x < 0: 
            logger.debug("Negative number, never a palindrome.")
            return False

        n_digits = self.count_digits(x)
        if n_digits % 2 == 0: 
            logger.debug("Even number of digits, palindrome if divisible by 11.")
            return (x % 11) == 0
        else: 
            return self.check_odd_number(x, n_digits)
    

    def count_digits(self, x: int) -> int:
        assert x >= 0
        return 1 if x == 0 else math.floor(math.log10(x)) + 1
    

    def check_odd_number(self, x: int, n_digits: int) -> bool:
        logger.debug("Odd number of digits, checking..")
        for i in range(n_digits//2):
            logger.debug(f"i, n_digits-1: {i, n_digits - i}")
            a = self.get_nth_digit(x, n_digits - i)
            b = self.get_nth_digit(x, i) 
            logger.debug(f"a, b: {a, b}")
            if a != b:
                logger.debug(f"Mismatch found at iteration i={i}: {a} != {b}.")
                return False
        logger.debug("No mismatch found. Is a palindrome.")
        return True

    
    # def get_nth_digit(self, x: int, n: int) -> int: 
    #     for _ in range(n-1):
    #         x = x // 10
    #     return x % 10
    
    def get_nth_digit(self, x: int, n: int) -> int: 
        if n == 0:
            _range = range(self.count_digits(x) - 1)
        else: 
            _range = range(n-1)

        # for _ in range(n-1):
        for _ in _range:
            x = x // 10
        return x % 10


test_cases: List[Tuple[str, bool]] = [
    (0, True),
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (5, True),
    (6, True),
    (7, True),
    (8, True),
    (9, True),
    (10, False),
    (11, True), 
    (12, False),
    (121, True),
    (134, False),
    (-1, False),
    (12321, True),
    (1234321, True),
    (123454321, True),
    (12345654321, True),
    (1234567890987654321, True),
]

run_test_cases(Solution().isPalindrome, test_cases)