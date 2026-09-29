# 713. Subarray Product Less Than K
  
<br>**Problem:** https://leetcode.com/problems/subarray-product-less-than-k/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search, Sliding Window, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-29 20:57 local time

**Runtime:** 33 ms (beats 47.127400000000016%)
**Memory:** 21.3 MB (beats 87.70649999999999%)


<!-- leetgit:submissionId=2157244629 codeHash=ff10f5893f4b214574ca43a4289129a8d9352369edb2c709cda86519a392fb7b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        product = 1
        result = 0
        right = 0
        n = len(nums)

        while right < n:
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            result += right - left + 1
            right += 1
        return result    
```
