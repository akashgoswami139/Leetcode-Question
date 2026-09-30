# 940. Fruit Into Baskets
  
<br>**Problem:** https://leetcode.com/problems/fruit-into-baskets/<br>

**Difficulty:** Medium<br>
**Topics:** Array, Hash Table, Sliding Window<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-10-01 00:44 local time

**Runtime:** 187 ms (beats 55.64119999999986%)
**Memory:** 25.9 MB (beats 64.75520000000003%)


<!-- leetgit:submissionId=2158541156 codeHash=5ef4e7d933b27d37b429e4d33b0a6ccc7efa0cad059d7a52f35cf333c77a7004 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        result = 0
        count = {}

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            result = max(result, right - left + 1)

        return result
```
