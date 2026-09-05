# 189. Rotate Array
  
<br>**Problem:** https://leetcode.com/problems/rotate-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Math, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-06 00:58 local time

**Runtime:** 172 ms (beats 8.091500000000005%)
**Memory:** 35.1 MB (beats 26.666400000000035%)


<!-- leetgit:submissionId=2132107395 codeHash=c5ed388a2461db14d3d451eeac0b4269c1bb4649730d176f536451262cfab00f notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if k>n-1:
            k = k%n
        def func(left,right):
            while left<right: 
                if n==1:
                    return
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
                left+=1
        func(0,len(nums)-1)  
        func(0,k-1)     
        func(k,len(nums)-1)
```
