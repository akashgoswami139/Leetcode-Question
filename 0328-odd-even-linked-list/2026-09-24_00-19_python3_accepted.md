# 328. Odd Even Linked List
  
<br>**Problem:** https://leetcode.com/problems/odd-even-linked-list/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-24 00:19 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 21.2 MB (beats 38.06909999999999%)


<!-- leetgit:submissionId=2151284919 codeHash=53d16c1f7b951fb66c91402cf756a070bac42eaa1d57e473dfdae979d5aa6209 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
```
