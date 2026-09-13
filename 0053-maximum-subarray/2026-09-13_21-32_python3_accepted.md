# 53. Maximum Subarray
  
<br>**Problem:** https://leetcode.com/problems/maximum-subarray/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Divide and Conquer, Dynamic Programming<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-13 21:32 local time

**Runtime:** 19 ms (beats 96.82609999999998%)
**Memory:** 31.4 MB (beats 44.918599999999984%)


<!-- leetgit:submissionId=2140771983 codeHash=440b83ca8800587f2a6cc49878d33de104b846fd362938cb0c851c9ddb7484a1 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

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
