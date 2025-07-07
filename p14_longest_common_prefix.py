"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
 

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List 


class Solution:
    """Optimized solver"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: 
            return strs[0]
        longest_prefix = ""
        i = 0
        while True: 
            for str in strs[1:]:
                try: 
                    if strs[0][i] == str[i]:
                        continue
                    else: 
                        return longest_prefix
                except IndexError:
                    return longest_prefix
            longest_prefix += strs[0][i]
            i += 1
                

test_cases = [
    (["flower", "flow", "flight"], "fl"), 
    (["dog", "racecar", "car"], "")
]

run_test_cases(Solution().longestCommonPrefix, test_cases)
