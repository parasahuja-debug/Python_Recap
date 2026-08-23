def hasCycle(self, head):
    if head is None or head.next is None:#check this
        return False

    slow = head #1
    fast = head.next #2

    while slow:
        if slow == fast:#true
            return True

        if fast is None or fast.next is None:#when list has an end
            return False

        slow = slow.next #move 1 point
        fast = fast.next.next #move 2 point

    return False #return false if while loop finishes and cannot meet means slow reached
#last but fast did not meet him

