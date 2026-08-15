# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            i_node=list1
            i=list1.val
        else:
            return list2
        if list2:
            j_node=list2
            j=list2.val
        else:
            return list1
        new=ListNode(val=-200)
        while i_node and j_node:
            if i==j:
                if new.val==-200:
                    new=i_node 
                    tmp=i_node.next if i_node.next else None
                    new.next=j_node
                    prev=j_node
                    i_node=tmp
                    j_node=j_node.next if j_node.next else None
                    j=j_node.val if j_node else 1000
                else:
                    prev.next=i_node
                    tmp=i_node.next if i_node.next else None
                    i_node.next=j_node
                    prev=j_node
                    i_node=tmp
                    j_node=j_node.next if j_node.next else None
                    i=i_node.val if i_node else 1000
                    j=j_node.val if j_node else 1000
                    
            elif i<j:
                if new.val==-200:
                    new=i_node
                    prev=new
                    i_node=i_node.next if i_node.next else None
                    i=i_node.val if i_node else 1000
                else:
                    prev.next=i_node
                    prev=i_node
                    i_node=i_node.next if i_node.next else None
                    i=i_node.val if i_node else 1000
            elif j<i:
                if new.val==-200:
                    new=j_node
                    prev=new
                    j_node=j_node.next if j_node.next else None
                    j=j_node.val if j_node else 1000
                else:
                    prev.next=j_node
                    prev=j_node
                    j_node=j_node.next if j_node.next else None
                    j=j_node.val if j_node else 1000
        if not i_node:
            prev.next=j_node if prev!=j_node else None
        else:
            prev.next=i_node if prev!=i_node else None
        return new



        