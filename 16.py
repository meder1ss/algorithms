def push(a, n):
    a.append(n)
    return a
def pop(a):
    el = a.pop(0)
    return a, el
def front(a):
    return a[0]
def size(a):
    return len(a)
def clear(a):
    a.clear()
    return a
queue = []
while 1:
    c = input()
    if "push" in c:
        c = c.split()
        queue = push(queue, int(c[1]))
        print('ok')
    if c == "pop":
        if size(queue) > 0:
            queue, el = pop(queue)
            print(el)
        else:
            print('error')
    if c == "front":
        if size(queue) > 0:
            print(front(queue))
        else:
            print('error')
    if c == "size":
        print(size(queue))
    if c == 'clear':
        queue = clear(queue)
        print('ok')
    if c == "exit":
        print('bye')
        break
    #print(queue)
