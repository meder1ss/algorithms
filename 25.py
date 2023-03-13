N = int(input())
s = list(map(int, input().split()))
s.sort()
sv = [[10**9,0]]
for i in range(1, N):
    a = min(sv[i - 1][0], sv[i - 1][1]) + (s[i] - s[i - 1])
    b = sv[i-1][0]
    sv.append([a,b])
print(sv[N-1][0])
