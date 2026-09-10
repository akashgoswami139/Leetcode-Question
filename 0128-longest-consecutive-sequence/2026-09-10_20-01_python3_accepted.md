# 128. Longest Consecutive Sequence
  
<br>**Problem:** https://leetcode.com/problems/longest-consecutive-sequence/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Union-Find<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-10 20:01 local time

**Runtime:** 59 ms (beats 23.649400000000053%)
**Memory:** 32.6 MB (beats 97.45070000000003%)


<!-- leetgit:submissionId=2137583590 codeHash=5fa22f11c7fc07ccf1781cb94faa68535a1ecaef2be6c68cbbe696904bfdd961 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        count = 1
        max_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1

            elif nums[i] == nums[i - 1]:
                continue

            else:
                count = 1

            max_count = max(max_count, count)

        return max_count
```
