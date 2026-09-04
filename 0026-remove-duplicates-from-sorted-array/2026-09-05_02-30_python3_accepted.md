# 26. Remove Duplicates from Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-05 02:30 local time

**Runtime:** 3 ms (beats 44.1706%)
**Memory:** 20.6 MB (beats 17.34979999999999%)


<!-- leetgit:submissionId=2131136789 codeHash=5c9a4a435fa8adeb57a9263a5c40cbd7673349c91fc99bfec2311e26c6b2e6d1 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n  = len(nums)
        new_dict= {}
        for i in range(0,len(nums)):
                new_dict[nums[i]]= 0
        count=0        
        for j in new_dict:
            nums.insert(count,j)
            count+=1

        return count
        
```
