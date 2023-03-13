def F(N, i):
    if i > N:
        return 3 * 10**4 + 1
    cost = a[N]
    if i <= 0:
        if N >= 1:
            if cost <= 100:
                res = min(F(N-1, i+1), F(N-1, i) + cost)
            else:
                return F(N-1, i+1)
        else:
            return 0
    else:
        if dp[N][i] != -1:
            return dp[N][i]
        if cost > 100:
            res = min(F(N-1, i+1), F(N-1, i-1) + cost)
        else:
            res = min(F(N-1, i+1), F(N-1, i) + cost)
    dp[N][i] = res
    return res

def days(u, N, k):
    if k < N:
        cost = a[N]
        if k <= 0 and N >= 1:
            if cost > 100:
                u.append(N)
                days(u, N - 1, k + 1)
            else:
                if F(N,k) == F(N-1, k+1):
                    u.append(N)
                    days(u, N-1, k+1)
                else:
                    days(u, N-1, k)
        else:
            state = (F(N, k) == F(N - 1, k + 1))
            if cost <= 100:
                if state:
                    u.append(N)
                    days(u, N-1, k+1)
                else:
                    days(u, N-1, k)
            else:
                if state:
                    u.append(N)
                    days(u, N-1, k+1)
                else:
                    days(u, N-1, k-1)
    return u
N = int(input())
a = [0]*(N+1)
for i in range(1, N+1):
    a[i] = int(input())
dp = [[0] * (N + 2) for i in range(N + 1)]
for i in range(0, N+1):
    for j in range(0, N+2):
        dp[i][j] = -1
ans = 3 * 10**4 + 1
for i in range(0,N+1):
    if ans >= F(N, i):
        ans = F(N, i)
        k1 = i
print(ans)
u = []
u = days(u, N, k1)
k2 = len(u)
print(k1, k2)
print(" ".join(map(str, sorted(u))))
