# 73. Set Matrix Zeroes
  
<br>**Problem:** https://leetcode.com/problems/set-matrix-zeroes/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Matrix<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-25 18:22 local time

**Runtime:** 239 ms (beats 10.47130000000004%)
**Memory:** 20.9 MB (beats 17.78360000000001%)


<!-- leetgit:submissionId=2152981354 codeHash=df2ecfb81e6283079776519eb4f17e15af4a54ea51e50431d2c3f715d6f22f3d notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        result = [row[:] for row in matrix]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:

                    # Set entire row to 0
                    for k in range(cols):
                        result[i][k] = 0

                    # Set entire column to 0
                    for k in range(rows):
                        result[k][j] = 0

        # Copy result back
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = result[i][j]
"""
Do not return anything, modify matrix in-place instead.
"""        
```
