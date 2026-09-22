# 142. Linked List Cycle II
  
<br>**Problem:** https://leetcode.com/problems/linked-list-cycle-ii/<br>

**Difficulty:** Medium<br>
**Topics:** Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-22 19:34 local time

**Runtime:** 60 ms (beats 13.91840000000001%)
**Memory:** 22.8 MB (beats 5.501699999999999%)


<!-- leetgit:submissionId=2149794323 codeHash=58b43f672d8ed8af0d448c40d5b1e941f8c30743c889a76058a7f64a571dc829 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dic={}

        while curr is not None:
            if curr in dic:
                return curr

            else:
                dic[curr]=dic.get(curr,0)+1
            curr= curr.next    
        return None      
```
