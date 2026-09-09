# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        dummy = ListNode(0)
        current = dummy
        i=0
        while i < len(lists) :
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
            i += 1
        while heap : 
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next :
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next



            


        




        
        