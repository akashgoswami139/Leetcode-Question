# 160. Intersection of Two Linked Lists
  
<br>**Problem:** https://leetcode.com/problems/intersection-of-two-linked-lists/<br>

**Difficulty:** Easy<br>
**Topics:** Hash Table, Linked List, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-27 23:00 local time

**Runtime:** 119 ms (beats 25.65479999999998%)
**Memory:** 38.1 MB (beats 55.40849999999998%)


<!-- leetgit:submissionId=2155215721 codeHash=9de2989f9d117feec82b0731bf0e7f9a48458ba654345d7f6a2441c8e01b9e93 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB

        while temp1 != temp2:
            if temp1 is None:
                temp1 = headB
            else:
                temp1 = temp1.next

            if temp2 is None:
                temp2 = headA
            else:
                temp2 = temp2.next

        return temp1
```
