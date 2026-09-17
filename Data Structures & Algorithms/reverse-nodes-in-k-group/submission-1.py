# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            KthNode = self.get_Kth_node(groupPrev, k)
            if not KthNode:
                break

            groupNext = KthNode.next

            # Reverse the list
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev 
                prev = curr
                curr = tmp


            # Connect the previous group with the reversed current group
            tmp = groupPrev.next
            groupPrev.next = KthNode
            groupPrev = tmp

        return dummy.next

    def get_Kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1

        return curr
        