# 485. Max Consecutive Ones
  
<br>**Problem:** https://leetcode.com/problems/max-consecutive-ones/<br>

**Difficulty:** Easy<br>
**Topics:** Array<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-07 21:41 local time

**Runtime:** 31 ms (beats 5.4634999999999945%)
**Memory:** 21.9 MB (beats 18.32900000000001%)


<!-- leetgit:submissionId=2134106072 codeHash=b3b70bdbfc7f6389195029470b45de9fa6ac2facabc4b9c56b7868dea5eb96bb notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count =0
        count=0
        for i in range(0,len(nums)):
            if nums[i] ==1:
                count+=1
            if nums[i]==0 or i == len(nums)-1:
                if count >= max_count:
                    max_count = count
                count = 0
        return max_count        
        
```
