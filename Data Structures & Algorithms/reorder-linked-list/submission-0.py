# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        col = []
        
        while head:
            col.append(head)
            head = head.next

        n = len(col)

        

        for i in range(n//2):
            col[i].next = col[-i-1]
            col[-i-1].next = col[i+1]

        col[n//2].next = None

        return col[0]

        