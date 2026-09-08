# 53. Maximum Subarray
  
<br>**Problem:** https://leetcode.com/problems/maximum-subarray/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Divide and Conquer, Dynamic Programming<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-08 12:39 local time

**Runtime:** 20 ms (beats 94.87770000000003%)
**Memory:** 31.3 MB (beats 74.31279999999998%)


<!-- leetgit:submissionId=2134795559 codeHash=12d3fa6ef598b417cd6fb10eb436ca9f2184b0a3fbbb695b50bba65a8d923ff3 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count =0
        max_count = float('-inf')
        n = len(nums)
        if n ==1:
            return nums[0]
        for i in range(0,n):
            count += nums[i]
            if max_count < count:
                max_count =count  
            if count <0:
                count = 0
              
        return max_count   
```
