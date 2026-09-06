# 283. Move Zeroes
  
<br>**Problem:** https://leetcode.com/problems/move-zeroes/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-06 10:56 local time

**Runtime:** 7 ms (beats 39.2382%)
**Memory:** 20.6 MB (beats 5.133200000000009%)


<!-- leetgit:submissionId=2132472290 codeHash=d7539d6ada78de5b341967e9dfd7410359328450bca5797a6a16f574d2ccb9e8 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        n= len(nums)
        for i in range(0,n):
            if nums[i]!=0:
                temp.append(nums[i])
        nums[:]=[0] * n        
        for i in range(0,len(temp)):
            nums[i]=temp[i]
            

                
        """
        Do not return anything, modify nums in-place instead.
        """
        
```
