# 242. Valid Anagram
  
<br>**Problem:** https://leetcode.com/problems/valid-anagram/<br>

**Difficulty:** Easy<br>
**Topics:** Hash Table, String, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-03 21:19 local time

**Runtime:** 12 ms (beats 55.55050000000001%)
**Memory:** 19.3 MB (beats 76.2278%)


<!-- leetgit:submissionId=2129788240 codeHash=079ffad933545dd83781e8a5157cdaceeb5f9895ec775423aa71e7844ceee5b3 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new={}
        new_tar={}
        if len(s)!= len(t):
            return False
        for i in s:
            new[i]=new.get(i,0)+1
        for j in t:
            new_tar[j]= new_tar.get(j,0)+1
        for k in new:    
            if new[k] != new_tar.get(k,0) :
                return False

        return True      
```
