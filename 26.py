size = input().split()
N = int(size[0])
M = int(size[1])
mat = []
for i in range(N):
    numbers = list(map(int, input().split()))
    mat.append(numbers)
answ = [[0 for x in range(M)] for y in range(N)]
answ[0][0] = mat[0][0]
for i in range(1, M):
    answ[0][i] = answ[0][i-1] + mat[0][i]
for i in range(1, N):
    answ[i][0] = answ[i-1][0] + mat[i][0]
for x in range(1, N):
    for y in range(1, M):
        answ[x][y] = min(answ[x][y-1], answ[x-1][y]) + mat[x][y]
print(answ[N-1][M-1])
