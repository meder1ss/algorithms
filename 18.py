def push_back(a, n):
    a.append(n)
    return a
def push_front(a, n):
    a.insert(0, n)
    return a
def pop_front(a):
    el = a.pop(0)
    return a, el
def pop_back(a):
    el = a.pop()
    return a, el
def back(a):
    return a[-1]
def front(a):
    return a[0]
def size(a):
    return len(a)
def clear(a):
    a.clear()
    return a
deque = []
while 1:
    c = input()
    if "push_front" in c:
        c = c.split()
        deque = push_front(deque, int(c[1]))
        print('ok')
    if "push_back" in c:
        c = c.split()
        deque = push_back(deque, int(c[1]))
        print('ok')
    if c == "pop_front":
        if size(deque) > 0:
            deque, el = pop_front(deque)
            print(el)
        else:
            print('error')
    if c == "pop_back":
        if size(deque) > 0:
            deque, el = pop_back(deque)
            print(el)
        else:
            print('error')
    if c == "front":
        if size(deque) > 0:
            print(front(deque))
        else:
            print('error')
    if c == "back":
        if size(deque) > 0:
            print(back(deque))
        else:
            print('error')
    if c == "size":
        print(size(deque))
    if c == 'clear':
        deque = clear(deque)
        print('ok')
    if c == "exit":
        print('bye')
        break
    #print(deque)
