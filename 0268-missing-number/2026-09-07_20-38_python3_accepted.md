# 268. Missing Number
  
<br>**Problem:** https://leetcode.com/problems/missing-number/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-07 20:38 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.3 MB (beats 75.41950000000001%)


<!-- leetgit:submissionId=2134032840 codeHash=0da15347018aa698e38b3798fc95b908f5368ca253aabeabd50fa5a991881a43 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = (n**2+n)//2
        result_2 = 0
        for i in range(0,len(nums)):
            result_2 += nums[i]
        return result- result_2
```
