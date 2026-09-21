# 141. Linked List Cycle
  
<br>**Problem:** https://leetcode.com/problems/linked-list-cycle/<br>

**Difficulty:** Easy<br>
**Topics:** Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-21 20:50 local time

**Runtime:** 52 ms (beats 66.60210000000001%)
**Memory:** 22.7 MB (beats 28.69209999999997%)


<!-- leetgit:submissionId=2148782209 codeHash=58a2fbadd79419f1eaf979252e68190db10074004ef9a5697f81041701349df2 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow= head
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast = fast.next.next
            if fast == slow:
                return True
 
        return False        
```
