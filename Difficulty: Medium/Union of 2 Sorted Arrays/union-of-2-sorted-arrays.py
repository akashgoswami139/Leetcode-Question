class Solution:
    def findUnion(self, a, b):
        n, m = len(a), len(b)
        i, j = 0, 0
        result = []

        while i < n and j < m:

            if a[i] < b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1

            elif b[j] < a[i]:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j += 1

            else:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1

        while i < n:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        while j < m:
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j += 1

        return result