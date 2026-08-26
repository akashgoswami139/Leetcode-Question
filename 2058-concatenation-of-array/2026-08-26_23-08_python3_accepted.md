# 2058. Concatenation of Array
  
<br>**Problem:** https://leetcode.com/problems/concatenation-of-array/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Simulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-26 23:08 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 78.6952%)


<!-- leetgit:submissionId=2121115000 codeHash=7063a3288d20a068420aa82925412f0bc5e61c870f916197ec38874c0b1b02ed notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        return nums + nums

test = Solution()
print(test.getConcatenation([1,2,1]))        
print(test.getConcatenation([1,3,2,1]))        
```
