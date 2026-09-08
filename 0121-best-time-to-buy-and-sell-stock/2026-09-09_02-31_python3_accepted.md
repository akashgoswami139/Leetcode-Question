# 121. Best Time to Buy and Sell Stock
  
<br>**Problem:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/<br>

**Difficulty:** Easy<br>
**Topics:** Array, Dynamic Programming<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-09 02:31 local time

**Runtime:** 36 ms (beats 76.8102%)
**Memory:** 28.7 MB (beats 21.304600000000015%)


<!-- leetgit:submissionId=2135635592 codeHash=cfd2a9d0cbe4f6093cc45d91d3b10dee9f124435f4741be9facedeaeabc1091f notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n =len(prices)
        min_price = float("inf")
        max_profit = 0
        profit =0
        for i in range(0,n):
            if min_price > prices[i]:
                min_price = prices[i]
            if min_price < prices[i]:
                profit = prices[i]- min_price
            if profit > max_profit:   
                max_profit = profit    
        if max_profit < 0:
            return 0
        return max_profit
```
