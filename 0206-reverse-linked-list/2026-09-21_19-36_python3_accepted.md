# 206. Reverse Linked List
  
<br>**Problem:** https://leetcode.com/problems/reverse-linked-list/<br>

**Difficulty:** Easy<br>
**Topics:** Linked List, Recursion<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-21 19:36 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.4 MB (beats 67.16510000000002%)


<!-- leetgit:submissionId=2148709583 codeHash=4cdecddd6ddb3e8abfa4075e0b6a9da08db125652f577e21eb6c115076591599 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp = head
        stack = []

        while temp is not None:
            stack.append(temp.val)
            temp = temp.next

        temp = head

        while temp is not None:
            e = stack.pop()
            temp.val = e
            temp = temp.next

        return head
```
