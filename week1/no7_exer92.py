# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode

        """
        p = head
        stack = []
        index = 1
        while p != None:
            if index >= left and index <= right:
                stack.append(p.val)
            p = p.next
            index += 1
        p = head
        index=1
        while p != None:
            if index >= left and index <= right:
                p.val = stack.pop()
            p = p.next
            index+=1
        return head
