# 448. Find All Numbers Disappeared in an Array
  
<br>**Problem:** https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-12 22:08 local time

**Runtime:** 47 ms (beats 20.1199%)
**Memory:** 31.2 MB (beats 20.170400000000058%)


<!-- leetgit:submissionId=2139789179 codeHash=e35690320791a773c82f32d3e620022c2de2220671b889c7c015806914dcf694 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Mark numbers that exist
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Find unmarked positions
        result = []

        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
```
