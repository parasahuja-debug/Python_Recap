class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        met = 0

        while fast and fast.next:
            if met == 0:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    met = 1
                    slow = head
                    if slow == fast:      # ADDED: catch the case where cycle start == meeting point
                        return slow
            else:
                slow = slow.next
                fast = fast.next

                if slow == fast:
                    return slow

        return None