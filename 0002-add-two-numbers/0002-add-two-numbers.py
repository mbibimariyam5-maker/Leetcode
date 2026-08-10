class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 and l2:
            v = l1.val + l2.val + carry

            carry = v // 10
            v = v % 10

            curr.next = ListNode(v)

            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            v = l1.val + carry

            carry = v // 10
            v = v % 10

            curr.next = ListNode(v)

            l1 = l1.next
            curr = curr.next

        while l2:
            v = l2.val + carry

            carry = v // 10
            v = v % 10

            curr.next = ListNode(v)

            l2 = l2.next
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next