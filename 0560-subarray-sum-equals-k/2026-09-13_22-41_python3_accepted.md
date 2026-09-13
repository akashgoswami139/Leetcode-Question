# 560. Subarray Sum Equals K
  
<br>**Problem:** https://leetcode.com/problems/subarray-sum-equals-k/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-13 22:41 local time

**Runtime:** 31 ms (beats 72.0111%)
**Memory:** 21.9 MB (beats 56.57400000000001%)


<!-- leetgit:submissionId=2140837952 codeHash=466d105ad1b8275791d685fd2f2f7c80d4af0325f589b1e286ac1e9f197b822a notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0

        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
```
