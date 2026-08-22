# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d=defaultdict(int)
        #first find length of the ll
        h=head
        # while head.next:
        #     nxt=head.next
        #     l=l+1
        #     head=head.next
        # print(l)
        # for i in range(0,l):
        #     nxt=h.next
        #     d[nxt]=d[nxt]+1
        #     h=nxt
        # if any(d)>1:
        #     return True
        # else:
        #     return False
        if not head:
            return False
        while all(value<=1 for value in d.values()) and h.next:
            nxt=h.next
            d[nxt]=d[nxt]+1
            h=nxt
        print(h.val)
        if any(value>1 for value in d.values()):
            return True
        else:
            return False        
        