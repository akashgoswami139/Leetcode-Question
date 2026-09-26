# 234. Palindrome Linked List
  
<br>**Problem:** https://leetcode.com/problems/palindrome-linked-list/<br>

**Difficulty:** Easy<br>
**Topics:** Linked List, Two Pointers, Stack, Recursion<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-26 21:29 local time

**Runtime:** 27 ms (beats 74.97289999999998%)
**Memory:** 53.6 MB (beats 24.723299999999995%)


<!-- leetgit:submissionId=2154121421 codeHash=d0dfa88d41c035a8bb86b7613b69d90e9a847b36bcf672f06b4b8e7626da7472 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        temp = head
        stack=[]
        while temp is not None:
            stack.append(temp.val)
            temp= temp.next


        temp= head

        while temp is not None:
            e = stack.pop()
            
            if e != temp.val:
                return False
            temp= temp.next
        return True                    
```
