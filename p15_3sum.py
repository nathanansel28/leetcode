"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
 

Constraints:
    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105

"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List, Tuple


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         l, m, r = 0, 1, 2
#         results = []


#         while l < len(nums) and m < len(nums) and r < len(nums):
#             left, mid, right = nums[l], nums[m], nums[r]
#             if left + mid + right == 0: 
#                 results.append([left, mid, right])

#     def update_index(self, l: int, m: int, r: int, n: int) -> Tuple[int, int, int]:
#         if r < n - 1: 
#             r += 1
#         elif m < n - 2: 
#             m += 1
#         elif l < n - 3:
#             l += 1 
#         else: 
#             return None, None, None # indicates that all indices have been explored
#         return l, m, r
    

class Solution:
    """Time Limit Exceeded"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        for i in range(len(nums) - 2):
            for j in range(len(nums) - 1):
                for k in range(len(nums)):
                    if i == j or i == k or j == k:
                        continue
                    left, mid, right = nums[i], nums[j], nums[k]
                    if left + mid + right == 0: 
                        results.append([left, mid, right])

        for result in results: 
            result.sort()
        
        logger.debug(f"threeSum -> results: {results}")
        unique_results = []

        for result in results: 
            if result not in unique_results: 
                unique_results.append(result)


        return unique_results


class Solution:
    """Better but not sufficiently."""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        for i in range(len(nums) - 2):
            for j in range(len(nums) - 1):
                for k in range(len(nums)):
                    if i == j or i == k or j == k:
                        continue
                    left, mid, right = nums[i], nums[j], nums[k]
                    if left + mid + right == 0:
                        candidate = sorted([left, mid, right]) 
                        if candidate not in results: 
                            results.append(candidate)

        return results


class Solution: 
    """2-pointer method."""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []

        # i, j, k = 0, 1, len(nums) - 1
        # while True:
        #     left, mid, right = nums[i], nums[j], nums[k]
        #     if left + mid + right == 0:
        #         candidate = sorted([left, mid, right])
        #         if candidate not in results: 
        #             results.append(candidate)
        previous_k = 10**6
        previous_i = 10**6
        previous_j = 10**6
        for k in range(len(nums) - 1, 0, -1):
            if k == previous_k:
                continue
            logger.debug(f"ITERATION k={k}")
            for i in range(k):
                if i == previous_i:
                    continue
                logger.debug(f"  ITERATION i={i}")
                for j in range(i+1, k):
                    if j == previous_j:
                        continue
                    left, mid, right = nums[i], nums[j], nums[k]
                    logger.debug(f"i,j,k: {i,j,k}  | left, mid, right = {left, mid, right}")
                    if left + mid + right == 0:
                        candidate = [left, mid, right]
                        if candidate not in results: 
                            results.append(candidate)
                            break
                    previous_j = j 
                previous_i = i
            previous_k = k
            
            
        return results


class Solution: 
    """2-pointer method."""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            j, k = i + 1, len(nums) - 1
            while j < k:

                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif current_sum < 0: 
                    j += 1
                else: 
                    k -= 1

        return results





def permutate(output: List):
    from itertools import permutations
    normalized = [tuple(sorted(triplet)) for triplet in output]    
    perms = set(permutations(normalized))
    return [ [list(t) for t in perm] for perm in perms ]


test_cases = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]), 
    ([0,1,1], []), 
    ([0,0,0], [[0,0,0]]),
]

test_cases = [(input, permutate(output)) for input, output in test_cases]

run_test_cases(Solution().threeSum, test_cases, passing_condition='in')