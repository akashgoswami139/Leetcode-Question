# 19. Remove Nth Node From End of List
  
<br>**Problem:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-24 13:43 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 92.06500000000001%)


<!-- leetgit:submissionId=2151762204 codeHash=af3874ee58572db9144b4340768aac0e9e3a5d8b75af792624912080dc2b28e0 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count=0
        temp =head
        while temp is not None:
            count+=1
            temp= temp.next

        
        if n ==count:
            head = head.next
            return head 

        temp = head

        for _ in range(count - n - 1):
            temp = temp.next

        temp.next = temp.next.next
        return head    
```
