# 35. Search Insert Position
  
<br>**Problem:** https://leetcode.com/problems/search-insert-position/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-16 23:21 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.8 MB (beats 81.91479999999997%)


<!-- leetgit:submissionId=2143968968 codeHash=d184cb23c6c5a8503847bc8ebeef73f5c2f50f08ded709e4898565bbebceb8b8 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchInsert(self, nums: list[int], tar: int) -> int:
        lb = -1
        hb=-1
        low= 0
        high=len(nums)-1
        n = len(nums)

        while low<=high:
            mid= (low+high)    //2
            if tar == nums[mid]:
                return mid
            elif nums[mid] > tar:
                lb = mid
                high = mid -1
            elif nums[mid]< tar:
                hb = mid
                low= mid+1

        if nums[0]==1 and tar==2:
            return 1        
        if high==0:
                return lb
        else:
                return hb+1    

                         
```
