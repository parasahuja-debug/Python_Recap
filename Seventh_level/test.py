class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next
        met = 0

        #while fast and fast.next:
        while slow:
            if slow==fast:
                if met==0:
                    met=1
                    slow=head
                else:
                    return slow
            
            if met==0:
                if fast.next is None or fast.next.next is None:
                    return None
                slow = slow.next
                fast = fast.next.next
            else:
                slow=slow.next
                fast=fast.next
        return None
        #     if met == 0:
        #         slow = slow.next
        #         fast = fast.next.next

        #         if slow == fast:
        #             met = 1
        #             slow = head
        #             if slow == fast:      # ADDED: catch the case where cycle start == meeting point
        #                 return slow
        #     else:
        #         slow = slow.next
        #         fast = fast.next

        #         if slow == fast:
        #             return slow

        # return None