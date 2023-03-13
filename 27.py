size = input().split()
N = int(size[0])
M = int(size[1])
mat = []
for i in range(N):
    numbers = list(map(int, input().split()))
    mat.append(numbers)
ways = [['' for x in range(M)] for y in range(N)]
answ = [[0 for x in range(M)] for y in range(N)]
answ[0][0] = mat[0][0]
for i in range(1, M):
    answ[0][i] = answ[0][i-1] + mat[0][i]
    ways[0][i] = 'R'*i
for i in range(1, N):
    answ[i][0] = answ[i-1][0] + mat[i][0]
    ways[i][0] = 'D'*i
for x in range(1, N):
    for y in range(1, M):
        a = answ[x][y-1]
        b = answ[x-1][y]
        if a > b:
            answ[x][y] = a + mat[x][y]
            ways[x][y] = ways[x][y-1] + 'R'
        else:
            answ[x][y] = b + mat[x][y]
            ways[x][y] = ways[x-1][y] + 'D'
print(answ[N-1][M-1])
print(" ".join(ways[N-1][M-1]))
