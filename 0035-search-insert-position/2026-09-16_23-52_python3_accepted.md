# 35. Search Insert Position
  
<br>**Problem:** https://leetcode.com/problems/search-insert-position/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-16 23:52 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.1 MB (beats 11.979899999999965%)


<!-- leetgit:submissionId=2144007271 codeHash=7c35a4aa144ef8cd15dc25c225fb48ce8d3bf5134dbb7c95c18d96bb472f043d notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchInsert(self, nums: list[int], tar: int) -> int:
        lb = -1
        hb = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if tar == nums[mid]:
                return mid

            elif nums[mid] >= tar:
                lb = mid
                high = mid - 1

            else:
                hb = mid
                low = mid + 1

        if lb != -1:
            return lb
        else:
            return hb + 1

```
