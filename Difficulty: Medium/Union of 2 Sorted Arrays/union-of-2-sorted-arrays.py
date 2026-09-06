class Solution:
    def findUnion(self, a, b):
        n,m= len(a),len(b)
        new= []
        i,j = 0,0
        while i<n and j<m:
            if a[i]==b[j]:
                if not new or new[-1] != a[i]:
                    new.append(a[i])
                i+=1
                j+=1
            elif a[i]> b[j]:
                if not new or new[-1] != b[j]:
                    new.append(b[j])
                j+=1
            elif a[i]< b[j]:
                if not new or new[-1] != a[i]:
                    new.append(a[i])
                i+=1
        for k in range(i, n):
            if not new or new[-1] != a[k]:
                new.append(a[k])
        for k in range(j, m):
            if not new or new[-1] != b[k]:
                    new.append(b[k])        
        return new