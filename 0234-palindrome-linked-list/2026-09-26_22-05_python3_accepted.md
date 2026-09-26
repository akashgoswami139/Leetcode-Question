# 234. Palindrome Linked List
  
<br>**Problem:** https://leetcode.com/problems/palindrome-linked-list/<br>

**Difficulty:** Easy<br>
**Topics:** Linked List, Two Pointers, Stack, Recursion<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-26 22:05 local time

**Runtime:** 40 ms (beats 37.11929999999999%)
**Memory:** 42.7 MB (beats 47.139199999999946%)


<!-- leetgit:submissionId=2154157773 codeHash=e0ad578b2a144c5a5a132cc85bf48d560ffa48986f467f3a2232b46696a18f94 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return True

        slow = fast = head

        # Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True    
```
