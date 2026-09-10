# 238. Product of Array Except Self
  
<br>**Problem:** https://leetcode.com/problems/product-of-array-except-self/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-11 00:30 local time

**Runtime:** 11 ms (beats 99.252%)
**Memory:** 25.6 MB (beats 53.86969999999998%)


<!-- leetgit:submissionId=2137886318 codeHash=24d0afaa63c44a61a4506ec61dfe5d3aeb2a50c3d1fd6c04e96cfe1bdaf45e95 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result
```
