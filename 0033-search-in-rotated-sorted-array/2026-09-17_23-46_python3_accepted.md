# 33. Search in Rotated Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/search-in-rotated-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-17 23:46 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.3 MB (beats 77.791%)


<!-- leetgit:submissionId=2145056533 codeHash=73cd9f5ce32ac5582941c72becff47a53416f358e413df0b4b70c4cc2d48b4b1 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i]== target:
                return i

            
        return -1    
```
