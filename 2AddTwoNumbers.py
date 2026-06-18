# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3 = ListNode()
        head = l3
        carry = 0

        while l1 is not None and l2 is not None:
            total = l1.val + l2.val + carry
            l3.val = total % 10
            carry = total // 10

            l1 = l1.next
            l2 = l2.next

            if l1 is not None or l2 is not None:
                l3.next = ListNode()
                l3 = l3.next

        while l1 is not None:
            total = l1.val + carry
            l3.val = total % 10
            carry = total // 10

            l1 = l1.next

            if l1 is not None:
                l3.next = ListNode()
                l3 = l3.next

        while l2 is not None:
            total = l2.val + carry
            l3.val = total % 10
            carry = total // 10

            l2 = l2.next

            if l2 is not None:
                l3.next = ListNode()
                l3 = l3.next

        if carry:
            l3.next = ListNode(carry)

        return head