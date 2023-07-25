# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1==None:
            return list2
        if list2==None:
            return list1
        if list1.val<=list2.val:
            p=list1
            q=p.next 
            t=list2 
        else:
            p=list2
            q=p.next 
            t=list1
        m=p
        while q!=None and t!=None:
            if q.val>=t.val:
                p.next=t
                t=t.next
                p.next.next=q 
                p=p.next
                
            elif q.val<t.val:
                p=q 
                q=q.next 
            
        if p.next==None:       
            p.next=t
        return m