# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev= None
        curr= head 
        if head is None or head.next is None:
            return None

        while curr :
            next_node=curr.next 
            curr.next = prev
            prev= curr
            curr=next_node
        if n == 1 :
            new_reversed_head = prev.next
        else : 
            new_reversed_head = prev
            temp = prev
            for _ in range(n-2):
                temp = temp.next
            
            temp.next=temp.next.next
        prev_back = None
        current_back=new_reversed_head
        while current_back :
            next_node = current_back.next
            current_back.next = prev_back
            prev_back = current_back
            current_back = next_node
            
        return prev_back


        