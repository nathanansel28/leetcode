"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

 
Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
 
    
Constraints:
    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List, Tuple


class Solution:
    """2-pointer method"""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 3):
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue  
            for j in range(i, len(nums) - 3):
                # if j > 0 and nums[j] == nums[j-1]:
                #     continue
                k, l = j + 1, len(nums) - 1

                while k < l:
                    logger.debug(f"i,j,k,l: {i, j, k, l}")
                    current_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if current_sum == target:
                        candidate = [nums[i], nums[j], nums[k], nums[l]]
                        candidate.sort()
                        # results.append(candidate)
                        candidate_idx = [i, j, k, l]
                        if len(set(candidate_idx)) == 4 and candidate not in results:
                            results.append(candidate)
                        # else: 
                            # logger.debug(f"candidate idx not distinct: {candidate_idx}")
                        
                        # while k < l and nums[k] == nums[k+1]:
                        #     k += 1
                        # while k < l and nums[l] == nums[l-1]:
                        #     l -= 1
                        
                        if l + 1 > j:
                            l-=1
                        else: 
                            k+=1
                    elif current_sum < target:
                        k += 1
                    else: 
                        l -= 1

        return results



def permutate(output: List):
    from itertools import permutations
    normalized = [tuple(sorted(triplet)) for triplet in output]    
    perms = set(permutations(normalized))
    return [ [list(t) for t in perm] for perm in perms ]

test_cases = [
    (([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]), 
    (([2,2,2,2,2], 8), [[2,2,2,2]]),
    (([0,0,0,0], 0), [[0,0,0,0]]),
]



test_cases = [(input, permutate(output)) for input, output in test_cases]

run_test_cases(Solution().fourSum, test_cases, passing_condition='in')