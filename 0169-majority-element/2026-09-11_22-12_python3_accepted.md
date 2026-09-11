# 169. Majority Element
  
<br>**Problem:** https://leetcode.com/problems/majority-element/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-11 22:12 local time

**Runtime:** 7 ms (beats 57.958699999999986%)
**Memory:** 21 MB (beats 98.0727%)


<!-- leetgit:submissionId=2138759233 codeHash=9329f9cf7ff83449a50f546cd40dd3c4d035c8d26349cbd5c8df62846e3bf6a5 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        value = 0
        for i in range(len(nums)):
            if count == 0:
                value = nums[i]
            if value == nums[i]:
                count += 1
            else:
                count -= 1

        return value
```
