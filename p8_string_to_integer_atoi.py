from typing import Tuple, List
from my_logger import load_logger
DEBUG = False
logger = load_logger(DEBUG)

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        s = s.strip()
        s = s.split()
        if len(s) > 0:
            s = s[0]
        else:
            return 0
        logger.debug(s)
        for i in range(len(s)):
            if i == 0 and (s[i] == "+" or s[i] == "-"):
                continue
            if not s[i].isnumeric():
                s1 = s[:i]
                break
            elif i == len(s) - 1: 
                s1 = s[:i+1]

        try:
            s1 = int(s1)
        except Exception as e:
            s1 = 0
            logger.error(f"Returning 0 for '{s}' due to exception: {e}")

        if s1 < -(2**31):
            s1 = -(2**31)
        elif s1 > 2**31 - 1:
            s1 = 2**31 - 1 

        logger.debug(s1)
        return int(s1)

solver = Solution()
test_cases: List[Tuple[str, int]] = [
    ('42', 42), 
    (' -042', -42), 
    ('1337c0d3', 1337),
    ('0-1', 0),
    ('words and 987', 0),
    (' -0122c3123190', -122),
    ('', 0)
]

for input, expected_output in test_cases: 
    actual_output = solver.myAtoi(input)
    assert actual_output == expected_output, f"Expecting {expected_output} got {actual_output}."
    logger.info("PASSED\n")