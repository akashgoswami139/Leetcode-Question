# 2271. Rearrange Array Elements by Sign
  
<br>**Problem:** https://leetcode.com/problems/rearrange-array-elements-by-sign/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-09 21:13 local time

**Runtime:** 65 ms (beats 24.9138%)
**Memory:** 44.5 MB (beats 13.449800000000002%)


<!-- leetgit:submissionId=2136520982 codeHash=04248259d2956effbd24d9b7141cd1f49a0ed435ab9cbace20e74facd2cc9e32 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        n = len(nums)
        result = []

        for i in range(0,n):
            if nums[i]> 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])    
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        
        return result
```
