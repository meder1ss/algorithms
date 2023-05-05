n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
diffs_all = {}
for i in range(n):
    for j in range(i+1, n):
        diffs_local = {}
        for a in mat[i]:
            for b in mat[j]:
                if abs(a-b) not in diffs_local.keys():
                    diffs_local[abs(a-b)] = 1
                else:
                    diffs_local[abs(a-b)] += 1
        for k in diffs_local.keys():
            if k not in diffs_all.keys():
                diffs_all[k] = diffs_local[k]
            else:
                diffs_all[k] += diffs_local[k]
summary = sum(diffs_all.values())
result = 0
#print(diffs_all)
#print(summary)
for k in diffs_all.keys():
    result += (diffs_all[k] * (k**3))/summary
print(result)