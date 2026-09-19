# 151. Reverse Words in a String
  
<br>**Problem:** https://leetcode.com/problems/reverse-words-in-a-string/<br>

**Difficulty:** Medium<br>
**Topics:** Two Pointers, String<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 16:50 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.5 MB (beats 11.653700000000004%)


<!-- leetgit:submissionId=2146588973 codeHash=447118cfa563f5230870cf6bfa55e0d85608de1ffa3a0691f53bb2a83fdb7d72 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        spl = s.split()
        reversed_str=''
        for i in range(len(spl)-1,-1,-1):
            reversed_str += spl[i]
            if i ==0:
                break
            reversed_str += " "

        return reversed_str        
```
