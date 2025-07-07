from typing import List, Tuple
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG = True
logger = load_logger(DEBUG)


class Solution:
    """Brute-force solution"""
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i+1:]):
                j += i + 1
                min_height = h1 if h1 < h2 else h2
                area = abs(i-j) * min_height
                logger.debug(f"i, j, h1, h2 = {i, j, h1, h2} -> area = {area}")
                if area >= max_area:
                    max_area = area
        
        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Improved height list, but doesn't solve runtime issue."""
        max_area = 0
        height = [(h, b) for b, h in enumerate(height)]
        height.sort()
        for idx, (h1, a) in enumerate(height):
            logger.debug(f"{height, height[idx+1:]}")
            for h2, b in height[idx+1:]:
                min_height = h1 if h1 < h2 else h2
                area = abs(a-b) * min_height
                logger.debug(f"a, b, h1, h2 = {a, b, h1, h2} -> area = {area}")
                if area >= max_area:
                    max_area = area
        
        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Two-Pointer Solution"""
        max_area = 0
        l, r = 0, len(height) - 1
        while True:
            h_left = height[l]
            h_right = height[r]
            min_height = h_left if h_left < h_right else h_right
            area = abs(l-r) * min_height
            logger.debug(f"l, r, h_l, h_r = {l, r, h_left, h_right} -> area = {area}")
            if area >= max_area:
                max_area = area
            if h_left >= h_right:
                r -= 1
            else: 
                l += 1
            if l == r: 
                break
        
        return max_area
        

test_cases: List[Tuple[List[int], float]] = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([2,1], 1)
]

run_test_cases(Solution().maxArea, test_cases)