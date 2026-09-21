# 141. Linked List Cycle
  
<br>**Problem:** https://leetcode.com/problems/linked-list-cycle/<br>

**Difficulty:** Easy<br>
**Topics:** Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-21 20:30 local time

**Runtime:** 54 ms (beats 54.117000000000004%)
**Memory:** 22.7 MB (beats 14.676899999999971%)


<!-- leetgit:submissionId=2148763279 codeHash=7aed6e4a1aadd14a5357d0845dd9e1a8d1e0197945948de0d00c3dbbf4d444c8 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        dic={}
        while temp is not None:
            if temp in dic:
                return True

            dic[temp]=1
            temp= temp.next    
        return False        
```
