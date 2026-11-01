class Solution:
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head

        # Find length
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        k = k % n

        if k == 0:
            return head

        # Reverse function
        def reverse(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        # Step 1: Reverse entire list
        head = reverse(head)

        # Step 2: Find the kth node
        curr = head

        for i in range(k - 1):
            curr = curr.next

        # Separate the two portions
        second = curr.next
        curr.next = None

        # Step 3: Reverse both portions
        first = reverse(head)
        second = reverse(second)

        # Step 4: Join both portions
        tail = first

        while tail.next:
            tail = tail.next

        tail.next = second

        return first