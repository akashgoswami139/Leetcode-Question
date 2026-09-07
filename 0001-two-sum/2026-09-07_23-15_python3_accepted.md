# 1. Two Sum
  
<br>**Problem:** https://leetcode.com/problems/two-sum/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-07 23:15 local time

**Runtime:** 1 ms (beats 61.1642%)
**Memory:** 20.6 MB (beats 18.442399999999985%)


<!-- leetgit:submissionId=2134235699 codeHash=cde7e6deebf6c5d792bf84d361757386a54e681512f3c9db680696c278e03b3c notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic ={}
        remains = 0
        n = len(nums)
        for i in range(0,n):
            remains = target - nums[i]
            if remains in dic:
                return i, dic[remains]
            dic[nums[i]]= dic.get(nums[i],i)+0
   

                         
```
