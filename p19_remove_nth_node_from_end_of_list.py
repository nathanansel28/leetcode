"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
 

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
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

import time 
class Solution:
    """Does NOT work."""
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        candidate_nodes = [None for _ in range(n+1)]
        current_head = head
        count = 1
        start = time.time()
        while time.time() - start < 30:
            logger.debug(f"\niteration {count}")
            logger.debug(f"candidate_nodes: {candidate_nodes}")
            # logger.debug(f"-n-1: {-n-1}")
            if current_head.next is None: 
                # if the end of the list has been reached
                logger.debug(f"End found!")
                logger.debug(f"  before n: {candidate_nodes[-n]}")
                logger.debug(f"  n-th node: {candidate_nodes[-n+1]}")
                logger.debug(f"  after n: {candidate_nodes[-n+2]}")
                
                if candidate_nodes[-n] is not None:
                    candidate_nodes[-n].next = candidate_nodes[-n+1].next
                else: 
                    logger.debug(f"candidate_nodes[-n] is None, candidate_nodes: {candidate_nodes}")

                if candidate_nodes[-n+1] is not None:
                    candidate_nodes[-n+1].next = None
                else: 
                    logger.debug(f"candidate_nodes[-n+1] is None, candidate_nodes: {candidate_nodes}")




                # if candidate_nodes[-n+1] is None:
                #    logger.debug("candidate_nodes[-n+1] is None")
                #    head = None 
                # else: 
                #     candidate_nodes[-n].next = candidate_nodes[-n+1].next # link the (n-1)-th node with the n-th node's next node 
                #     candidate_nodes[-n+1].next = None # un-link the n-th node from the back
                break
            else: 
                candidate_nodes = [candidate_nodes[i+1] for i in range(len(candidate_nodes)-1)]
                candidate_nodes.append(current_head)
                current_head = current_head.next 
                logger.debug(f"End not reached yet, candidate_nodes: {candidate_nodes}")

            count += 1
        return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        slow, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next
        while True: 
            if fast.next is None: 
                slow.next = slow.next.next 
                break
            else: 
                slow = slow.next
                fast = fast.next 
        
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
def wrapped_solution(input_list: List[float], n: int) -> List[float]:
    head = list_to_linked_list(input_list)
    result_head = Solution().removeNthFromEnd(head, n)
    return linked_list_to_list(result_head)

test_cases = [
    (([1, 2, 3, 4, 5], 2), [1, 2, 3, 5]),
    (([1, 2, 3, 4, 5, 6, 7, 8], 2), [1, 2, 3, 4, 5, 6, 8]),
    (([1], 1), []),
    (([1, 2], 1), [1]),
]

# Run the tests
run_test_cases(wrapped_solution, test_cases, passing_condition='equal')
