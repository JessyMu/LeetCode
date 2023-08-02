# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        p=head
        if p==None:
            return None
        if p.next==None:
            m=Node(p.val)
            if p.random==p:
                m.random=m
            return m
        m=Node(p.val)
        head2=m
        map={p:m}
        while p.next!=None:
            n=Node(p.next.val)
            m.next=n
            m=m.next
            p=p.next
            map.update({p:m})
        p=head
        m=head2
        while p!=None:
            if p.random==None:
                m.random=None
            else:
                m.random=map[p.random]
            p=p.next
            m=m.next
        return head2

        