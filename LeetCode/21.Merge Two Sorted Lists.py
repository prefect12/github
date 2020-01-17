# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:


Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

class Solution:

    def mergeTwoLists(self, l1, l2):
        new_link = current = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                current.next, l1 = l1, l1.next
            else:
                current.next, l2 = l2, l2.next
            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return new_link.next
