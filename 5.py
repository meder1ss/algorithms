N = int(input())
a = int(input())
good = 0
for i in range(1, N):
    b = int(input())
    good += min(a, b)
    a = b
print(good)
