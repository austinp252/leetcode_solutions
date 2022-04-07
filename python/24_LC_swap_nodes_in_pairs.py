# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # get pair
        # get first
        # check if second
        # swap
        # update previous pair next to this
        # set current pair to previous pair

        prevPairTail = None
        currentPairHead = head
        head = currentPairHead
        if(head):
            while(True):
                if(currentPairHead.next):
                    currentPairTail = currentPairHead.next
                else:
                    break

                currentPairHead.next = currentPairTail.next  # set head to tail
                currentPairTail.next = currentPairHead  # set tail to front
                if(prevPairTail):  # set previous pair next to updated swapped values
                    prevPairTail.next = currentPairTail
                else:
                    head = currentPairTail

                if(currentPairHead.next):
                    prevPairTail = currentPairHead  # update previous tail to current tail
                    currentPairHead = currentPairHead.next  # update current to start of next pair
                else:
                    break
        return head
