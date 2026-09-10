# 49. Group Anagrams
  
<br>**Problem:** https://leetcode.com/problems/group-anagrams/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, String, Sorting<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-10 22:38 local time

**Runtime:** 15 ms (beats 41.18389999999998%)
**Memory:** 24.1 MB (beats 9.71810000000001%)


<!-- leetgit:submissionId=2137755858 codeHash=714859e364d80976bf23be79955908cc88ecb0a9fb314d55680c876a51e8f5a9 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for strr in strs:
            count = [0] * 26
            for ch in strr:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            if key in dic:
                dic[key].append(strr)
            else:
                dic[key] = [strr]
        return list(dic.values())    
```
