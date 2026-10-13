# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def addTwoNumbers(self, linkedList1, linkedList2):
        """
            :type linkedList1: Optional[ListNode]
            :type linkedList2: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        l = ListNode(0)
        curr = l
        h1 = linkedList1
        h2 = linkedList2
        carry = 0
        while h1 or h2 or carry:
            x = h1.data if h1 else 0
            y = h2.data if h2 else 0    
            total = x + y + carry
            carry = total//10
            digit = total%10

            curr.next = ListNode(digit)
            curr = curr.next
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next
       
        return l.next
        

