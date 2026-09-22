# 142. Linked List Cycle II
  
<br>**Problem:** https://leetcode.com/problems/linked-list-cycle-ii/<br>

**Difficulty:** Medium<br>
**Topics:** Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-22 19:52 local time

**Runtime:** 47 ms (beats 85.8123%)
**Memory:** 22.2 MB (beats 95.7517%)


<!-- leetgit:submissionId=2149814180 codeHash=595702b728055b31918bdb2efe1cc79c8d6e7ddfe88a211d3cfa8e161f5ad1a7 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None and fast.next is not None :
            slow= slow.next
            fast= fast.next.next 

            if slow == fast:
                slow= head
                
                while fast !=  slow:
                    
                    slow= slow.next
                    fast= fast.next 

                return fast
                     
        return None      
```
