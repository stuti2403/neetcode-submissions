# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        a=head.next
        if not a:
            return head
        b=a.next
        a.next=head
        head.next=None
        head=a
        a=b
        if a:
            while a.next:
                b=a.next
                tmp=b
                a.next=head 
                head=a
                a=tmp
            a.next=head
            return a
        return head
        

        

        
           
        