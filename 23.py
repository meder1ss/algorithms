def f(n):
    cache = [0] * (n + 1)
    for i in range(2, n + 1):
        v = cache[i - 1]
        if i % 2 == 0:
            v = min(v, cache[i // 2])
        if i % 3 == 0:
            v = min(v, cache[i // 3])
        cache[i] = v + 1
    return cache

def numbers(cache, n):
    op = cache[-1]
    num = n
    numbers = ''
    for _ in range(op):
        v = cache[num - 1]
        num_l = num-1
        if num % 2 == 0:
            if v > cache[num // 2]:
                num_l = num // 2
        if num % 3 == 0:
            if v > cache[num // 3]:
                num_l = num // 3
        numbers += str(num_l)[::-1] + " "
        num = num_l
    return op, numbers[::-1]

N = int(input())
op, numbers = numbers(f(N), N)
print(op)
if numbers[1:]:
    print(numbers[1:] + " " + str(N))
else:
    print(str(N))
