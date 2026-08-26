# 344. Reverse String
  
<br>**Problem:** https://leetcode.com/problems/reverse-string/<br>

**Difficulty:** Easy<br>
**Topics:** Two Pointers, String<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-26 21:26 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 23.4 MB (beats 81.0468%)


<!-- leetgit:submissionId=2120990562 codeHash=6c3f7fb721b4546158d599c3286af96915d77b8ce9a1ace1be59d1dc640a3b40 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        reverse_s = []

        for i in range(len(s) - 1, -1, -1):
            reverse_s.append(s[i])

        for i in range(len(s)):
            s[i] = reverse_s[i]

Input1 = ["h", "e", "l", "l", "o"]
Input2 = ["H", "a", "n", "n", "a", "h"]

ex1 = Solution()

ex1.reverseString(Input1)
ex1.reverseString(Input2)

print(Input1)
print(Input2)            
```
