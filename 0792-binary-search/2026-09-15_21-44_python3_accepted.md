# 792. Binary Search
  
<br>**Problem:** https://leetcode.com/problems/binary-search/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-15 21:44 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 20.4 MB (beats 76.67580000000001%)


<!-- leetgit:submissionId=2142795361 codeHash=c74d09887b83503ca9561d405af91ef4fd12098b6d2a7c1d650c3c8f75fbaaab notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid= (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1    
        return -1       

```
