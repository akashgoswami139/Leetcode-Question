# 560. Subarray Sum Equals K
  
<br>**Problem:** https://leetcode.com/problems/subarray-sum-equals-k/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-13 22:51 local time

**Runtime:** 31 ms (beats 72.0111%)
**Memory:** 21.8 MB (beats 56.57400000000001%)


<!-- leetgit:submissionId=2140847853 codeHash=64b4b728158c66e75df0189e54fa329cc5f7e3ceea66344dbb8c981e37f88bdc notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        count = 0

        # Stores: prefix_sum -> how many times we have seen it
        seen = {}
        seen[0] = 1

        for num in nums:

            # Add current number to running sum
            prefix_sum = prefix_sum + num

            # Find the prefix sum we need
            needed = prefix_sum - k

            # If we have seen it before, we found subarray(s)
            if needed in seen:
                count = count + seen[needed]

            # Store current prefix sum
            if prefix_sum in seen:
                seen[prefix_sum] = seen[prefix_sum] + 1
            else:
                seen[prefix_sum] = 1

        return count
```
