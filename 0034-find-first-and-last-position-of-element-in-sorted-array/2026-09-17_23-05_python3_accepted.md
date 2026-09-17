# 34. Find First and Last Position of Element in Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-17 23:05 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.7 MB (beats 8.602699999999988%)


<!-- leetgit:submissionId=2145007034 codeHash=376791b2ecd1e665f797655ad0a27fa7c3768955c2eb8073a6e14e4555b1b263 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = -1
        hb = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                lb =mid
                high =mid-1
            else:
                low= mid+1
        if lb == -1 or nums[lb] != target:
            return [-1,-1]     
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] <= target:
                hb =mid
                low =mid+1
            else:
                high= mid-1
        
        else:    
            return [lb,hb]

```
