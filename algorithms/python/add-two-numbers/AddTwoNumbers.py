"""
    Source: https://leetcode.com/problems/add-two-numbers/
    Date: 02/11/2021
    Author: Prasaanth Selvakumar


*****************************************************************************
Question:
You are given two non-empty linked lists representing two 
non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example 1: 
	Input: l1 = [2,4,3], l2 = [5,6,4]
	Output: [7,0,8]
	Explanation: 342 + 465 = 807.

Example 2:
	Input: l1 = [0], l2 = [0]
	Output: [0]

Example 3:
	Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
	Output: [8,9,9,9,0,0,0,1]


Constrints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that 
    does not have leading zeros.

"""

### Solution ####
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = l1.val + l2.val
        rem = val//10
        out_node = ListNode(val%10)
        head = out_node
        l1 = l1.next
        l2 = l2.next
        
        while not(l1 is None or l2 is None):
            val = l1.val + l2.val + rem
            rem = val//10
            out_node.next = ListNode(val%10)
            l1 = l1.next
            l2 = l2.next
            out_node = out_node.next
        if l1 is None:
            if l2 is None:
                if rem!=0:
                    out_node.next = ListNode(rem)
            else:
                while l2 is not None:
                    val = l2.val + rem
                    rem= val//10
                    out_node.next = ListNode(val%10)
                    l2 = l2.next
                    out_node = out_node.next
                    if(rem == 0):
                        out_node.next = l2
                        break
                else:
                    if rem!=0:
                        out_node.next = ListNode(rem)
        else:
            if l1 is None:
                if rem!=0:
                    out_node.next = ListNode(rem)
            else:
                while l1 is not None:
                    val = l1.val + rem
                    rem = val//10
                    out_node.next = ListNode(val%10)
                    l1 = l1.next
                    out_node = out_node.next
                    if(rem == 0):
                        out_node.next = l1
                        break
                else:
                    if rem!=0:
                        out_node.next = ListNode(rem)
        return head
