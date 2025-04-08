# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=1
        temp=head
        while temp.next!=None:
            temp=temp.next
            count+=1
        temp=head
        if count==n:
            return head.next
        else:
            for i in range(count-n-1):
                temp=temp.next
            temp.next=temp.next.next
            return head
            