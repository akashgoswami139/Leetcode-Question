# 153. Find Minimum in Rotated Sorted Array
  
<br>**Problem:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-20 19:24 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.5 MB (beats 27.1723%)


<!-- leetgit:submissionId=2147740361 codeHash=1a32a6cf3b50054eeda6d5e87ac0e9b603e7961682429a52183fc280679dc406 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def findMin(self, nums: list[int]) -> int:
        low= 0
        n= len(nums)
        high = n-1
        min=float('inf')

        while low<= high:
            mid = (low+high)//2

            if nums[low] <= nums[mid]:

                if min > nums[mid]:
                    min = nums[mid]

                if nums[mid] >= nums[high]:
                    low = mid+1
                else:
                    high = mid-1   

            elif nums[mid]>= nums[high]:

                if min > nums[mid]:
                    min = nums[mid]

                if nums[mid]>= nums[high]:
                    low = mid+1

                else:
                    high = mid-1
            elif nums[low]> nums[mid] <nums[high]:
                min = nums[mid]

                low+=1
                high-1


        return min                          

```
