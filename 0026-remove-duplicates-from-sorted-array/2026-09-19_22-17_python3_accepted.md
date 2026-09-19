# 26. Remove Duplicates from Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 22:17 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.4 MB (beats 97.24130000000001%)


<!-- leetgit:submissionId=2146848713 codeHash=28f047beeaf838eb6c65e181c6b19308ce79b7cc0a4e2015cfd310a5dea1f17e notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left =0
        n = len(nums)
        count =0
        uniqq=float('-inf')


        while left < n:
            if uniqq < nums[left]:
                nums[count]= nums[left]
                uniqq = nums[left]
                count+=1
                left+=1
            else:
                left+=1  

        return count        
```
