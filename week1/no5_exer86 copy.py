# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        m=head
        n=m.next 
        q=None
        p=None
        l=None
        HEAD=True
        while n!=None:
            if n.val>=x:
                if HEAD:
                    HEAD=False
                    l=n 
                    p=n
                else:
                    q=n
                    p.next=q
                    p=q
                m.next=n.next
                n=n.next
            else:
                m=n 
                n=n.next 
        if p!=None:
            p.next=None
        if head.val>=x:
            q=head
            head=head.next
            m.next=q
            m=m.next
        m.next=l
        return head
