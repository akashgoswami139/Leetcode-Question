# 347. Top K Frequent Elements
  
<br>**Problem:** https://leetcode.com/problems/top-k-frequent-elements/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-10 23:08 local time

**Runtime:** 3 ms (beats 89.91720000000001%)
**Memory:** 22.8 MB (beats 80.65369999999999%)


<!-- leetgit:submissionId=2137793824 codeHash=e4a31546d3e77c9f688495c18320804699173ab872c5ed7bcd51ddce42b9c57b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        value =0
        dic= {}
        n= len(nums)
        for i in range(0,n):
            dic[nums[i]]=dic.get(nums[i],0)+1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        new = list(dic.keys())    
        for j in range(0,k):
            out.append(new[j])
        return out

```
