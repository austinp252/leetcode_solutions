# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # brute force - first glance
        # one pass to get list of nodes
        # use algo to determine if list is a palindrome
        nodes = []
        curNode = head
        while(True):
            nodes.append(curNode.val)
            if(curNode.next):
                curNode = curNode.next
            else:
                break
        # list should be established
        # algo for determining if list is a palindrome
        for index, val in enumerate(nodes[:len(nodes)/2]):
            if not (nodes[index] == nodes[len(nodes)-1-index]):
                return False
        return True
