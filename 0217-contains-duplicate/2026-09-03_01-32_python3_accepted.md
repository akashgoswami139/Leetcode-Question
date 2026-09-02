# 217. Contains Duplicate
  
<br>**Problem:** https://leetcode.com/problems/contains-duplicate/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-03 01:32 local time

**Runtime:** 10 ms (beats 84.36239999999998%)
**Memory:** 32.5 MB (beats 22.402900000000034%)


<!-- leetgit:submissionId=2128930701 codeHash=4d6e1b0e6e04ee2ee9b4bf4dfdeea6c7e0848282b325bc74c32e8ac408b39f70 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

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
