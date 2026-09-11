# 75. Sort Colors
  
<br>**Problem:** https://leetcode.com/problems/sort-colors/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Sorting, Quicksort, Bubble Sort<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-11 22:46 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.5 MB (beats 23.572199999999988%)


<!-- leetgit:submissionId=2138796380 codeHash=a8fff88d0b4a1528d6ed0cda1adb92b1c551a18e1e4bbcac947c6ad2a07fdafa notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        min= 0

        for i in range(0,len(nums)):
            min=0
            for j in range(i+1, len(nums)):
                if nums[i]> nums[j]:
                    min= j
                    nums[i] ,nums[min]  =nums[min]  ,nums[i]     
        """
        Do not return anything, modify nums in-place instead.
        """
```
