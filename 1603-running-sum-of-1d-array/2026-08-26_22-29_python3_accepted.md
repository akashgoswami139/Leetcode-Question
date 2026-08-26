# 1603. Running Sum of 1d Array
  
<br>**Problem:** https://leetcode.com/problems/running-sum-of-1d-array/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Prefix Sum<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-26 22:29 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.9 MB (beats 11.014700000000019%)


<!-- leetgit:submissionId=2121064474 codeHash=d02be80312b411e3d63e0c45898089510853b04fa2a49b2b0df2978afe6d891a notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.new_nums = []

        def add(left=0, total=0):
            if left == len(nums):
                return

            total += nums[left]
            self.new_nums.append(total)

            add(left + 1, total)

        add()

        return self.new_nums  

input1 = [1,2,3,4]
input2 = [1,1,1,1,1]
input3 = [3,1,2,10,1]

ex1=Solution()
print(ex1.runningSum(input1))
print(ex1.runningSum(input2))
print(ex1.runningSum(input3))


        
```
