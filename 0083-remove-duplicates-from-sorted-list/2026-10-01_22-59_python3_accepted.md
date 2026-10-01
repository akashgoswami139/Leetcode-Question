# 83. Remove Duplicates from Sorted List
  
<br>**Problem:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/<br>

**Difficulty:** Easy<br>
**Topics:** Linked List<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-10-01 22:59 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.3 MB (beats 31.928900000000013%)


<!-- leetgit:submissionId=2159459916 codeHash=2241eaef655cc18c20fb72bcffd4e1cb9185357928e20b52ee394e247642d80c notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return head

        prev = head
        temp = head.next

        while temp is not None:
            if prev.val == temp.val:
                prev.next = temp.next
            else:
                prev = temp

            temp = temp.next

        return head
```
