# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getLen(self,list):
        head = list 
        len=0
        while head!=None:
            len+=1
            head=head.next
        return len
    def move(self,list,dist):
        head=list
        while dist>0:
            head=head.next
            dist-=1
        return head
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA=self.getLen(headA)
        lenB=self.getLen(headB)
        dist=lenA-lenB
        if dist>0:
            listA=self.move(headA,dist)
            listB=headB
        elif dist<0:
            listA=headA
            listB=self.move(headB,abs(dist))
        else:
            listA=headA
            listB=headB
        while listA!=None:
            if listA==listB:
                return listA
            listA=listA.next
            listB=listB.next

        return None
    