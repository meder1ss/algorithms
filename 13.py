def solve(vr):
    st = []
    for w in vr:
        if w.isdigit():
            st.append(int(w))
            continue
        y = st.pop()
        x = st.pop()
        z = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y }[w](x, y)
        st.append(z)
    return st.pop()

vr = input().split()
print(solve(vr))
