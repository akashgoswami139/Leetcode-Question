# 169. Majority Element
  
<br>**Problem:** https://leetcode.com/problems/majority-element/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-11 20:28 local time

**Runtime:** 11 ms (beats 33.23569999999999%)
**Memory:** 21.2 MB (beats 47.391999999999996%)


<!-- leetgit:submissionId=2138659493 codeHash=7657d0c028ebd1b9a4979a39a49cb4c500b751b3a3a9ff32493478a61b21b2e3 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        n= len(nums)    
        for i in range(0,n):
            dic[nums[i]]=dic.get(nums[i],0)+1
        count=0
        new= 0
        for j in dic:
            if dic[j] > count:
                count= dic[j]
                new= j
        return new    
```
