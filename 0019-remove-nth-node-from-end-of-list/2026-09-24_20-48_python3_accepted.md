# 19. Remove Nth Node From End of List
  
<br>**Problem:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-24 20:48 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 92.06500000000001%)


<!-- leetgit:submissionId=2152121973 codeHash=db810f3311b610fb9e3dc7450467cd950d5db730924bf16017f89f9010c9f06c notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        fast = head
        slow= head
        


        for _ in range(n):
            fast = fast.next

        if fast == None:
            head = head.next
            return head    

        while fast.next is not None:
            fast= fast.next
            slow= slow.next

        slow.next= slow.next.next

        return head    
```
