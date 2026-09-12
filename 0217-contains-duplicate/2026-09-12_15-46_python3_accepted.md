# 217. Contains Duplicate
  
<br>**Problem:** https://leetcode.com/problems/contains-duplicate/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-12 15:46 local time

**Runtime:** 23 ms (beats 28.449000000000005%)
**Memory:** 32.1 MB (beats 79.4205%)


<!-- leetgit:submissionId=2139380006 codeHash=0c724c01da2af4b6f1f2794885665c773e48437e8fc5289e36ad1ba39b34da3b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
```
