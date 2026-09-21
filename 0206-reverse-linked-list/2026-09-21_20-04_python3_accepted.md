# 206. Reverse Linked List
  
<br>**Problem:** https://leetcode.com/problems/reverse-linked-list/<br>

**Difficulty:** Easy<br>
**Topics:** Linked List, Recursion<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-21 20:04 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.6 MB (beats 29.156700000000022%)


<!-- leetgit:submissionId=2148738217 codeHash=cbe1fc38b9c5f441e7c5921929f333fcafb41648e51a14feaed0a8f586f38438 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp = head
        pre= None
        


        while temp is not None:
            front = temp.next
            temp.next= pre
            pre = temp
            temp = front

        head = pre
        return head
```
