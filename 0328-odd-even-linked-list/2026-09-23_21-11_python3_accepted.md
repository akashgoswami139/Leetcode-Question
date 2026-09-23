# 328. Odd Even Linked List
  
<br>**Problem:** https://leetcode.com/problems/odd-even-linked-list/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-23 21:11 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 21.1 MB (beats 76.88409999999999%)


<!-- leetgit:submissionId=2151055585 codeHash=6f25571aade09f08701906fa6f75d12585279dd5970b6319b8ee3f8e62d63479 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or  head.next is None:
            return head


        scack=[]
        curr= head
        while curr is not None:
            
            scack.append(curr.val)
            if curr.next is None:
                break
            curr=curr.next.next


        curr= head.next 

        while curr is not None :
            if curr.next is None:
                break
            
            scack.append(curr.val)
            curr=curr.next.next
        curr = head
        index=0
        while curr is not None :
            if index > len(scack)-1:
                break
            curr.val= scack[index]
            index+=1
            curr= curr.next       
        return head


                
        
        
```
