# 128. Longest Consecutive Sequence
  
<br>**Problem:** https://leetcode.com/problems/longest-consecutive-sequence/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Union-Find<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-09 23:52 local time

**Runtime:** 48 ms (beats 63.03960000000002%)
**Memory:** 36.7 MB (beats 20.09500000000002%)


<!-- leetgit:submissionId=2136734301 codeHash=56489d1ce59d1efc3eaeba2ab39cb1c1b96df2314a4c606e405118d5bd491e2d notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for num in num_set:

            if num - 1 not in num_set:

                count = 1
                current = num

                while current + 1 in num_set:
                    current += 1
                    count += 1

                max_count = max(max_count, count)

        return max_count                                 
```
