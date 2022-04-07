# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # first item has no .next value
        # subsequent items have next value of previously parsed item
        # single pass
        prevNode = None
        curNode = head
        if not (curNode):
            return
        while(True):
            # start with head of origninal LL, iterate with each pass (curnode)
            # prevNode set in previous pass or outside loop, last item in original LL

            # condition to check if original LL cannot be iterated, set new head to updated value
            newNode = ListNode()
            newNode.val = curNode.val
            newNode.next = prevNode
            if(curNode.next):
                prevNode = newNode
                curNode = curNode.next
            else:
                newHead = newNode
                break
        return newHead
