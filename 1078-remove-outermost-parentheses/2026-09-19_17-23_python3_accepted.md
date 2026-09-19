# 1078. Remove Outermost Parentheses
  
<br>**Problem:** https://leetcode.com/problems/remove-outermost-parentheses/<br>

**Difficulty:** Easy<br>
**Topics:** String, Stack, Bracket Sequences<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 17:23 local time

**Runtime:** 4 ms (beats 22.61230000000002%)
**Memory:** 19.3 MB (beats 70.51699999999998%)


<!-- leetgit:submissionId=2146611392 codeHash=b1ba68025b0a1a38b0d7686b88d3d24664fae1f0a4135d9a6278b2bf368263f2 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        value=""
        for i in s:
            if i =="(":
                count+=1
               
                if count > 1:
                    value += i

            elif i ==")":
                count-=1

                if count > 0:
                    value += i
            
            
        return value                
            
        
```
