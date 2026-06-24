from itertools import combinations

w=[2,3,1]
v=[4,5,3]
cap=4
best=0

for r in range(4):
    for s in combinations(range(3),r):
        if sum(w[i] for i in s)<=cap:
            val=sum(v[i] for i in s)
            if val>best:
                best=val
                ans=s

print("Selection:",list(ans))
print("Value:",best)
