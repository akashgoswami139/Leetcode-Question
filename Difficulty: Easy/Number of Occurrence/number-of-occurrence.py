class Solution:
    def countFreq(self, arr, target):
        low =0
        n = len(arr)
        high = n-1
        count= 0
        for i in arr:
            if i ==target:
                count+=1
        return count        
        