# 283. Move Zeroes
  
<br>**Problem:** https://leetcode.com/problems/move-zeroes/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-06 01:45 local time

**Runtime:** 711 ms (beats 5.273800000000015%)
**Memory:** 20.4 MB (beats 89.8812%)


<!-- leetgit:submissionId=2132137145 codeHash=6ae9e797733f59013e8222778a10029c7687f3a078913ba0a241c7c93ab967f1 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(0,len(nums)):
            if nums[i]==0:
                n =nums.remove(nums[i])
                nums.append(0)                
        """
        Do not return anything, modify nums in-place instead.
        """
        
```
