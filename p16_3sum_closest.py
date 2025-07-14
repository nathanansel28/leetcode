"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:
    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104

"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List, Tuple

class Solution:
    """2-pointer method."""
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_sum = None

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            j, k = i + 1, len(nums) - 1
            while j < k:

                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum - target == 0:
                    logger.debug(f"Found best best_sum from {nums[i], nums[j], nums[k]}")
                    return current_sum
                elif current_sum - target < 0: 
                    j += 1
                else: 
                    k -= 1

                if best_sum is None: 
                    best_sum = current_sum
                    logger.debug(f"Found first best_sum from {nums[i], nums[j], nums[k]}")

                elif abs(current_sum - target) < abs(best_sum - target):
                    best_sum = current_sum
                    logger.debug(f"Found better best_sum from {nums[i], nums[j], nums[k]}")

        return best_sum


class Solution:
    """2-pointer method, optimized"""
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        logger.debug(f"nums sorted: {nums}")
        best_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            j, k = i + 1, len(nums) - 1
            logger.debug(f"\nITERATION {i, j, k}: {nums[i], nums[j], nums[k]}")
            while j < k:
                logger.debug(f"current ijk: {i,j,k}")
                current_sum = nums[i] + nums[j] + nums[k]

                if abs(current_sum - target) < abs(best_sum - target):
                    best_sum = current_sum
                elif current_sum < target:
                    j += 1
                elif current_sum > target: 
                    k -= 1
                else: 
                    return current_sum

        return best_sum

        
test_cases: List[Tuple[Tuple[List[int], int], int]] = [
    ( ([-1,2,1,-4], 1), 2 ),
    ( ([0,0,0], 1), 0 ),
    ( ([4,0,5,-5,3,3,0,-4,-5], -2), -2 ),
    ( ([-4,2,2,3,3,3], 0), 0 ), 
    ( ([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -14), -15 )
]

run_test_cases(Solution().threeSumClosest, test_cases, passing_condition='equal')