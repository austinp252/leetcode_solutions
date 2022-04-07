# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # result node: l1 + l2 % 10
        #remainder: l1 + l2 / 10

        # end condition when both LL reach tail (next = null)

        # get valid nodes at each pass
        # advance nodes at each pass

        # for each node, check if exists
        # if exists, add to sum and advance to next node
        # save result of result % 10 in current result node

        #

        # how to initialize start/each new node
        # if not end, init node at beginning of pass to 0 + remainder
        # init prevnode to null, conditional that if not prevnode null prev.next = current
        # handle end condition
        # both LL reach tail (neither LL has next and remainder is 0)
        #otherwise, this = remainder + 0 + values

        resultHead = None
        prevNode = None
        remainder = 0

        while(True):
            if(l1 or l2 or (remainder != 0)):  # create new result node, not end
                curVal = 0+remainder
                curNode = ListNode(0, None)
                if(prevNode):
                    prevNode.next = curNode
                else:
                    resultHead = curNode

                if(l1):
                    curVal += l1.val
                    l1 = l1.next
                if(l2):
                    curVal += l2.val
                    l2 = l2.next

                curNode.val = curVal % 10
                remainder = curVal / 10
                prevNode = curNode
            else:
                return resultHead
