# 34. Find First and Last Position of Element in Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-17 11:47 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.6 MB (beats 61.940499999999986%)


<!-- leetgit:submissionId=2144398473 codeHash=cf459983b8ff07245846095860266bac3d5f3fc146c632cd9e4e7f0052890a78 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = -1
        hb = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                lb = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                hb = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [lb, hb]
```
