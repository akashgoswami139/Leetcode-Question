# 268. Missing Number
  
<br>**Problem:** https://leetcode.com/problems/missing-number/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-07 20:02 local time

**Runtime:** 1407 ms (beats 6.432099999999918%)
**Memory:** 20.6 MB (beats 19.040500000000012%)


<!-- leetgit:submissionId=2133993229 codeHash=161195ccb7fa9558e74ab3cd4fc83faa22a09c5c8868606c1129b74a3cedf9aa notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n+1):
            if i not in nums:
                return i 
```
