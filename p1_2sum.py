"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
 

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_idx = [(i, num) for i, num in enumerate(nums)]
        nums_with_idx.sort(key=lambda x: x[1])
        logger.debug(nums_with_idx)
        nums_indices = [num[0] for num in nums_with_idx]
        nums = [num[1] for num in nums_with_idx]

        left, right = 0, len(nums) - 1
        while left < right: 
            current_sum = nums[left] + nums[right]
            logger.debug(f"{nums[left]} {nums[right]} -> {current_sum}")
            if current_sum == target:
                return [nums_indices[left], nums_indices[right]]
            elif current_sum < target: 
                logger.debug("shifting right")
                left += 1
            else: 
                logger.debug("shifting left")                
                right -= 1

def permutate(output: List[int]):
    from itertools import permutations
    return [list(p) for p in permutations(output)]

test_cases = [
    ( ([2,7,11,15], 9), [0,1] ), 
    ( ([3,2,4], 6), [1,2] ), 
    ( ([3,3], 6), [0,1] ), 
    ( ([3,2,3], 6), [0,2])
]


test_cases = [(input, permutate(output)) for input, output in test_cases]

run_test_cases(Solution().twoSum, test_cases, passing_condition='in')