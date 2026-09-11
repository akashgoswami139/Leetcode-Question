# 75. Sort Colors
  
<br>**Problem:** https://leetcode.com/problems/sort-colors/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Two Pointers, Sorting, Quicksort, Bubble Sort<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-12 00:30 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 62.46349999999999%)


<!-- leetgit:submissionId=2138901835 codeHash=4e6af9f22467f22511fe7413666902559aba7c2dfb3a40c20787ef04474990cb notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0
        mid = 0
        high =len(nums)-1   
        for i in range(0,len(nums)):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low += 1
                mid += 1   
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]    
                high-=1           
        """
        Do not return anything, modify nums in-place instead.
        """
```
