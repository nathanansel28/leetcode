"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
 

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)
from typing import List, Tuple, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    """Working but not optimal version."""
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None: 
            return 
        if list1 is None: 
            return list2
        if list2 is None:
            return list1
        dummy = ListNode(val=None, next=None)
        current_head = dummy

        while True: 
            logger.debug(f"current_head: {current_head}")
            if list1.val <= list2.val:
                current_head.next = list1
                current_head = current_head.next
                list1 = list1.next
            
            else: 
                current_head.next = list2
                current_head = current_head.next
                list2 = list2.next

            if list1 is None: 
                current_head.next = list2 
                break
            if list2 is None:
                current_head.next = list1 
                break

            if list1.next is None and list2.next is None: 
                if list1.val <= list2.val: 
                    current_head.next = list1
                    current_head.next.next = list2
                else: 
                    current_head.next = list2
                    current_head.next.next = list1
                break


        logger.debug(f"current_head and its next: {current_head}, {current_head.next}")
        logger.debug(f"dummy and its next and next: {dummy}, {dummy.next}, {dummy.next.next}")

        return dummy.next
    

def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    head = None
    for val in reversed(lst):
        head = ListNode(val=val, next=head)
    return head

def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Wrapper around the solution to match expected input/output
def wrapped_solution(list1, list2) -> List[float]:
    head1 = list_to_linked_list(list1)
    head2 = list_to_linked_list(list2)
    result_head = Solution().mergeTwoLists(head1, head2)
    return linked_list_to_list(result_head)

test_cases = [
    ( ([1,2,4], [1,3,4]), [1,1,2,3,4,4] ),
    ( ([], []), [] ),
    ( ([], [0]), [0] ),
    ( ([2], [1]), [1,2] )
]


run_test_cases(wrapped_solution, test_cases, passing_condition='equal')

