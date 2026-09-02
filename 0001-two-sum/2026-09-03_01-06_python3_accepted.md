# 1. Two Sum
  
<br>**Problem:** https://leetcode.com/problems/two-sum/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-03 01:06 local time

**Runtime:** 1715 ms (beats 28.50499999999914%)
**Memory:** 19.7 MB (beats 95.15350000000001%)


<!-- leetgit:submissionId=2128912957 codeHash=8891c1e833cd9c11dc321b679f2097de1dcd9850f0d99b3b1ecda503feb3efde notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]== target:
                    return i,j
      
```
