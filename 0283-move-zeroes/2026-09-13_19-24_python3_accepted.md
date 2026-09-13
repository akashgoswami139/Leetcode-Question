# 283. Move Zeroes
  
<br>**Problem:** https://leetcode.com/problems/move-zeroes/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-13 19:24 local time

**Runtime:** 3 ms (beats 81.7325%)
**Memory:** 20.6 MB (beats 25.36959999999999%)


<!-- leetgit:submissionId=2140661865 codeHash=91ff963f0814cc088a994c73621b30367a3b6a27adf5bf8bd67df23ade7934f4 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left= 0
        n =len(nums)
        if 0 not in nums:
            return nums
        for i in  range(0,n):
            if nums[i]!= 0:
                nums[left],nums[i]= nums[i], nums[left]
                left+=1

        """
        Do not return anything, modify nums in-place instead.
        """
        
```
