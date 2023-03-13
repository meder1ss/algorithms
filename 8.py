N = int(input())
minx = miny = 10**9
maxx = maxy = -10**9
for i in range(N):
    l = input().split()
    x = int(l[0])
    y = int(l[1])
    maxx = max(x, maxx)
    minx = min(x, minx)
    maxy = max(y, maxy)
    miny = min(y, miny)
print(minx, miny, maxx, maxy)
