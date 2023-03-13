def numways(s, r, cache):
    if s < 0:
        return 0
    if s == 0:
        return 1
    res = 0
    for i in range(1, min(s+1, r+1)):
        if cache[s-i] == 0:
            cache[s-i] = numways(s - i, r, cache)
        res += cache[s - i]
    return res

s = input().split()
N = int(s[0])
k = int(s[1])
print(numways(N-1, k, [0]*(N+1)))
