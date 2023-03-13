def let_cnt(x, N): 
    if x > N/2:
        x = N - x 
    return N*x - x*x 

s = list(input())
answ = {}
len = len(s)
for i in range(0, len): 
    if s[i] == '\0': 
        continue 
    cnt = let_cnt(i+1, len+1)
    for j in range(i+1, len):
        if s[j] == s[i]: 
            cnt += let_cnt(j+1, len+1)
            s[j] = '\0'
    answ[s[i]] = cnt 
answ = {key:answ[key] for key in sorted(answ.keys())}
for i in answ.keys(): 
    print(str(i) + ": " + str(answ[i]))
