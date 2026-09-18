# 81. Search in Rotated Sorted Array II
  
<br>**Problem:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-18 10:15 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.6 MB (beats 32.96880000000001%)


<!-- leetgit:submissionId=2145355966 codeHash=952e2da1209be1935bd9ff334d6e111d8d56e402a6a9c56eb7e6f4e7044cb9d0 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # Duplicate case
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1

            # Left half is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            elif nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
```
