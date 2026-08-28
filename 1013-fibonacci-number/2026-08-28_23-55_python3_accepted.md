# 1013. Fibonacci Number
  
<br>**Problem:** https://leetcode.com/problems/fibonacci-number/<br>

**Difficulty:** Easy<br>
**Topics:** Math, Dynamic Programming, Recursion, Memoization<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-28 23:55 local time

**Runtime:** 54 ms (beats 42.44439999999998%)
**Memory:** 19.3 MB (beats 19.38020000000001%)


<!-- leetgit:submissionId=2123199668 codeHash=fccfcff0a4486c599f8a46e349ff0d2369c3dd02d4c9251d08e58d86ab5d30ba notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1

        for _ in range(n):
            a, b = b, a + b

        return a
```
