# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return None

        length = 0

        temp = head

        while temp:
            length += 1

            temp = temp.next

        print(length)

        i = 1
        
        temp = head
        if length - n == 0:
            return head.next

        while i < length - n:
            temp = temp.next
            i +=1

        temp.next = temp.next.next

        return head

        