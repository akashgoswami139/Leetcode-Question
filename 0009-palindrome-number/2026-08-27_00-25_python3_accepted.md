# 9. Palindrome Number
  
<br>**Problem:** https://leetcode.com/problems/palindrome-number/<br>

**Difficulty:** Easy<br>
**Topics:** Math<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-08-27 00:25 local time

**Runtime:** 8 ms (beats 53.82350000000001%)
**Memory:** 19.2 MB (beats 87.1954%)


<!-- leetgit:submissionId=2121207603 codeHash=e8a3ebe9bbbbbc6edc0ffdfa7285b2540470b20d9cf8fb9578626e16f069de3b notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        orignal = x
        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        return reverse == orignal    
                
text = Solution()
print(text.isPalindrome(121))
print(text.isPalindrome(-121))
print(text.isPalindrome(10))
```
