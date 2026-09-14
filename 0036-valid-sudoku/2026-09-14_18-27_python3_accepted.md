# 36. Valid Sudoku
  
<br>**Problem:** https://leetcode.com/problems/valid-sudoku/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Matrix<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-14 18:27 local time

**Runtime:** 7 ms (beats 27.989000000000008%)
**Memory:** 19.4 MB (beats 10.333400000000012%)


<!-- leetgit:submissionId=2141567272 codeHash=24ba495323b1ce05b605c8a4267a2474380fe23e84f45ce28f2fcdefbb8b4b27 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for i in range(9):
            seen = set()

            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])

        
        for j in range(9):
            seen = set()

            for i in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])

        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                seen = set()

                for i in range(r, r + 3):
                    for j in range(c, c + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] in seen:
                            return False

                        seen.add(board[i][j])

        return True
```
