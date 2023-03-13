import sys
s = input()
stack = []
for b in s:
    if b == "(" or b == "[" or b == "{":
        stack.append(b)
    elif b == " ":
        continue
    else:
        try:
            el = stack.pop()
        except IndexError:
            print('no')
            sys.exit()
            #break
        if (el == "(" and b != ")") or (el == "[" and b != "]") or (el == "{" and b != "}"):
            print('no')
            sys.exit()
            #break
    #print(stack)
if stack:
    print('no')
else:
    print('yes')
