# 167. Two Sum II - Input Array Is Sorted
  
<br>**Problem:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 21:37 local time

**Runtime:** 11 ms (beats 6.174099999999999%)
**Memory:** 22.3 MB (beats 11.273500000000006%)


<!-- leetgit:submissionId=2146811163 codeHash=f4056e0d76bda4f2f5c279e8c5855824f94edb5c56a56e9ac08ee70b2afcdede notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
            total = numbers[low] + numbers[high]

            if total == target:
                return [low + 1, high + 1]

            elif total < target:
                low += 1

            else:
                high -= 1
```
