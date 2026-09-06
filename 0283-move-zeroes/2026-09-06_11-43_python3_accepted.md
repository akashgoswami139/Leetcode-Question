# 283. Move Zeroes
  
<br>**Problem:** https://leetcode.com/problems/move-zeroes/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-06 11:43 local time

**Runtime:** 6 ms (beats 43.8797%)
**Memory:** 20.4 MB (beats 89.8812%)


<!-- leetgit:submissionId=2132515502 codeHash=f379a583a29c2df9c2d7b4cb67e55b12008eec309dd0e431e717619ebdecbf13 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1                  
        """
        Do not return anything, modify nums in-place instead.
        """
        
```
