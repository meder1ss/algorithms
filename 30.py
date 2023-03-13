N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
F = [[0] * (M + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if a[i - 1] == b[j - 1]:
            F[i][j] = F[i - 1][j - 1] + 1
        else:
            F[i][j] = max(F[i - 1][j], F[i][j - 1])
Ans = []
i = N
j = M
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        Ans.append(a[i - 1])
        i -= 1
        j -= 1
    elif F[i - 1][j] == F[i][j]:
        i -= 1
    else:
        j -= 1
Ans = Ans[::-1]
print(" ".join(map(str, Ans)))
