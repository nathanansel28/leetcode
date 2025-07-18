"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 
Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List, Tuple, Optional


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def greater_or_equal(list1, list2):
            """Returns True if all elements in list1 is >= than all elements in list2"""
            if len(list1) == 0 or len(list2) == 0:
                return False
            return all(x >= max(list2) for x in list1)

        def lesser_or_equal(list1, list2): 
            """Returns True if all elements in list1 is <= than all elements in list2"""
            if len(list1) == 0 or len(list2) == 0:
                return False
            return all(x <= min(list2) for x in list1)
 
        """convention: nums1 is shorter than nums2"""
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(A), len(B)

        i = m // 2
        while i <= m:
            j = (m + n + 1)  / 2 - i
            logger.debug(f"i,j = {i}, {int(j)}")
            # if not isinstance(j, int):
            #     logger.debug(f"warning: j is not an int")    
            # j = int(j)
            logger.debug(f"   check: B[:j+1] >= A[:i]: {A[:i], B[:j+1]} -> {lesser_or_equal(A[:i], B[:j+1])}")
            logger.debug(f"   check: A[i:] >= B[j:]: {A[i:], B[:j]} -> {greater_or_equal(A[i:], B[:j])}")
            if greater_or_equal(B[:j+1], A[:i]) and greater_or_equal(A[i:], B[:j]):
                logger.debug(f"\nReturning: i:{i} -> {A[i]}")
                return A[i]
            elif not lesser_or_equal(A[:i], B[:j+1]):
                logger.debug("shifting i left")
                i -= 1
            else: 
                logger.debug("shifting i right")
                i += 1



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """convention: nums1 is shorter than nums2"""
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(A), len(B)

        i = m // 2

        if (m + n) % 2 == 1: 
            while i <= m:
                j = (m + n + 1)  / 2 - i
                logger.debug(f"i,j = {i}, {int(j)}")

                if :
                    logger.debug(f"\nReturning: i:{i} -> {A[i]}")
                    return A[i]
                elif not lesser_or_equal(A[:i], B[:j+1]):
                    logger.debug("shifting i left")
                    i -= 1
                else: 
                    logger.debug("shifting i right")
                    i += 1



test_cases = [
    ( ([3,4], [1,2,4,5]), 3.5 ),
    ( ([1,3], [2]), 2 ),
    ( ([1,2], [3,4]), 2.5 ),
    ( ([3,4], [3,4]), 3.5 ),
    ( ([1], [1]), 1 ),
    ( (list(range(1,100)), list(range(1,100))), 50 ),
    ( (list(range(1,1000)), list(range(1,1000))), 500 ),
]


run_test_cases(Solution().findMedianSortedArrays, test_cases, description="Median of Two Sorted Arrays")
