# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # Approach 1
        # Idea is to find length of the list and return list from middle node
        # Time Complexity: O(n) | Space Complexity: O(1)
        if not head:
            return []

        len = 0
        temp = head
        while temp:
            len+=1
            temp = temp.next
        
        temp = head
        len = len//2
        print(len)
        while len > 0:
            len-=1
            temp = temp.next
        return temp
        '''

        # Approach 2
        # Traverse nodes with two pointers, head will visit each node fast will goes alternate
        # The time fast will reach at end, head will be at middle node
        # Time Complexity: O(n) | Space Complexity: O(1)
        fast = head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            head = head.next
        
        return head
