# 1046. Max Consecutive Ones III
  
<br>**Problem:** https://leetcode.com/problems/max-consecutive-ones-iii/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search, Sliding Window, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-28 21:59 local time

**Runtime:** 60 ms (beats 48.22480000000001%)
**Memory:** 22.2 MB (beats 51.84050000000001%)


<!-- leetgit:submissionId=2156201703 codeHash=672b44166bdad71de0459cdccc17d6c1fa35e336b3bde039fa50aec8a322e32b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count 
```
