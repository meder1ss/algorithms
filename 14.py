s = []
op = []
n = int(input())
tr = list(map(int, input().split()))
num = 1
for val in tr:
    if len(s) > 0 and val > s[len(s) - 1]:
        print("NO")
        quit(0)
    op.append(1)
    s.append(val)
    while len(s) > 0 and s[len(s) - 1] == num:
        op.append(2)
        s.pop()
        num += 1
print("YES")
