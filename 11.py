stack = []
while 1:
    s = input()
    if 'push' in s:
        s = s.split()
        stack.append(s[1])
        print('ok')
    elif s == 'pop':
        try:
            e = stack.pop()
            print(e)
        except IndexError:
            print('error')
    elif s == 'back':
        try:
            e = stack[-1]
            print(e)
        except IndexError:
            print('error')
    elif s == 'size':
        print(len(stack))
    elif s == 'clear':
        stack.clear()
        print('ok')
    elif s == 'exit':
        print('bye')
        break
    else:
        print('wrong command!')
