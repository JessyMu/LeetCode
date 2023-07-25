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
        if head==None or head.next == None:
            return head 
        p=head.next
        head.next = None
        while p.next != None :
            q=p.next
            p.next = head 
            head=p
            p=q 
            

        p.next=head 
        return p
        

