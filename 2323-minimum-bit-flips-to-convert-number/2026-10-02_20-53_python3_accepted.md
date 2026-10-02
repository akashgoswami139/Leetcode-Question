# 2323. Minimum Bit Flips to Convert Number
  
<br>**Problem:** https://leetcode.com/problems/minimum-bit-flips-to-convert-number/<br>

**Difficulty:** Easy<br>
**Topics:** Bit Manipulation<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-10-02 20:53 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.4 MB (beats 7.837999999999994%)


<!-- leetgit:submissionId=2160278978 codeHash=523fa311ed761c53d9a144dad65b73bb234ac8886a6a23a4dc04db6dd3e63d50 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start^goal).count('1')
```
