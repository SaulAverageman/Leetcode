# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=0
        h1=headA
        while h1:
            l1+=1
            h1=h1.next
        l2=0
        h2=headB
        while h2:
            l2+=1
            h2=h2.next
        if l1>l2:
            for i in range(l1-l2):
                headA=headA.next
        else:
            for i in range(l2-l1):
                headB=headB.next
        #print(headA.val,headB.val)
        while headA:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None