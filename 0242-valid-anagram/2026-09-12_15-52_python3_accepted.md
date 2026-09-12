# 242. Valid Anagram
  
<br>**Problem:** https://leetcode.com/problems/valid-anagram/<br>

**Difficulty:** Easy<br>
**Topics:** Hash Table, String, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-12 15:52 local time

**Runtime:** 12 ms (beats 55.2017%)
**Memory:** 19.4 MB (beats 76.0461%)


<!-- leetgit:submissionId=2139384238 codeHash=d82ece0478a3784917a706c89addb1224a314e004e1a0255fbb8b3145ec36d45 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new={}
        new_tar={}
        if len(s) != len(t):
            return False
        for i in s:
            new[i]= new.get(i,0)+1
        for j in t:
            new_tar[j]= new_tar.get(j,0)+1 
        for k in new:
            if new[k] != new_tar.get(k,0):
                return False 
        return True      
```
