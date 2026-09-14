# 48. Rotate Image
  
<br>**Problem:** https://leetcode.com/problems/rotate-image/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Math, Matrix<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-14 19:21 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.3 MB (beats 69.11769999999999%)


<!-- leetgit:submissionId=2141615300 codeHash=39391460d2cacf115573ecd9cc1c8182976f08c3a3a4fbe25ba20058425689cd notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        cols = len(matrix[0])
        row =len(matrix)
    
        for i in range(row):
            for j in range(i+1,cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        
        for i in range(row):
            left = 0
            right = cols - 1

            while left < right:
                matrix[i][left], matrix[i][right] = \
                    matrix[i][right], matrix[i][left]

                left += 1
                right -= 1
        """
        Do not return anything, modify matrix in-place instead.
        """
        
```
