# 908. Middle of the Linked List
  
<br>**Problem:** https://leetcode.com/problems/middle-of-the-linked-list/<br>

**Difficulty:** Easy<br>
**Topics:** Linked List, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-21 18:41 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.3 MB (beats 59.5933%)


<!-- leetgit:submissionId=2148656105 codeHash=5714614c7d7504bd3a59ca1c12a8285d11796a332306fc221e4c87a90e322d19 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow  
        
```
