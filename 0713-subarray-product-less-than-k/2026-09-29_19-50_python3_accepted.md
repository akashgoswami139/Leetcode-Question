# 713. Subarray Product Less Than K
  
<br>**Problem:** https://leetcode.com/problems/subarray-product-less-than-k/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search, Sliding Window, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-29 19:50 local time

**Runtime:** 24 ms (beats 86.94610000000002%)
**Memory:** 21.6 MB (beats 6.2270999999999965%)


<!-- leetgit:submissionId=2157174162 codeHash=90299b3170b64f36a7cb7c7236c4bac527f4b6a09d9eb9320f90777cfe42adbd notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        result = 0
        n = len(nums)

        for right in range(n):
            product *= nums[right]              # expand window to the right

            while product >= k and left <= right:   # shrink window from left until valid
                product //= nums[left]
                left += 1

            result += (right - left) + 1           # count all valid subarrays ending at r

        return result
```
