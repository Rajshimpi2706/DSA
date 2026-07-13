class Solution(object):
    def mergeTwoLists(self, list1, list2):

        # Create a dummy node
        dummy = ListNode()

        # Pointer to build the merged list
        current = dummy

        # Compare nodes from both lists
        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the merged list
        return dummy.next