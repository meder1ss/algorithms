f = open('input.txt')
n = int(f.readline())
a = [[] for _ in range(n)]
d = [10**9]*n
for i in range(n):
    a[i] = list(map(int, f.readline().split()))
line = f.readline().split()
s = int(line[0])-1
f = int(line[1])-1
d[s] = 0
queue = [s]
while queue:
    i = queue.pop()
    for j in range(n):
        if a[i][j] and d[j] > d[i]+1:
            d[j] = d[i] + 1
            queue.append(j)
if d[f] < 10**9:
    print(d[f])
else:
    print(-1)
