# 74. Search a 2D Matrix
  
<br>**Problem:** https://leetcode.com/problems/search-a-2d-matrix/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Binary Search, Matrix<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 22:40 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.5 MB (beats 80.1385%)


<!-- leetgit:submissionId=2146871380 codeHash=1e390ef961e05c32db6b1d86e10fa0209d57867860c1f32e1392e20b973f5a19 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low =0
        row = len(matrix)
        col= len(matrix[0])

        high=( row*col)-1

        while low<=high:
            mid= (low+high)//2

            i_c = mid % col
            j_r = mid // col

            if matrix[j_r][i_c]==target:
                return True

            elif matrix[j_r][i_c] >= target:
                high = mid-1
            else:
                low= mid+1    
        return False
```
