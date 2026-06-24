from itertools import permutations

c=[[3,10,7],[8,5,12],[4,6,9]]
m=999

for p in permutations(range(3)):
    t=sum(c[i][p[i]] for i in range(3))
    if t<m:
        m=t
        a=p

print("Assignment:",a)
print("Cost:",m)
