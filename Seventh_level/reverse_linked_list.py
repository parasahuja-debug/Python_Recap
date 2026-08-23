class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save next node
            curr.next = prev        # reverse the link
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev

# 1-2-3-4-5
# head on 1
# well 5 is pointing to null
# now for reverse 1 should point to null
    
# initialise prev as null
# current as 1

# save the position of next
# move current pointer to prev
# make prev as current
# current as next