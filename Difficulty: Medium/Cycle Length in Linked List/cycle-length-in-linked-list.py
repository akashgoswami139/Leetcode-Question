''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        slow= head
        fast=head
        
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow= slow.next
        

            if fast == slow:
                
                current = slow.next
                count=1
                
                while current != slow:
                    current = current.next
                    count += 1
                return count  
                
        return 0