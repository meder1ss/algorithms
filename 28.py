size = input().split()
N = int(size[0])
M = int(size[1])
answ = [[0 for x in range(M)] for y in range(N)]
answ[0][0] = 1
for x in range(1, N):
    for y in range(1, M):
        res = 0
        if x >= 2:
            res += answ[x-2][y-1]
        if y >= 2:
            res += answ[x-1][y-2]
        answ[x][y] = res
print(answ[N-1][M-1] )
