from itertools import permutations

c=[(1,2),(4,5),(7,1),(3,6)]
s=c[0]
m=999

for p in permutations(c[1:]):
    path=[s]+list(p)+[s]
    d=0
    for i in range(len(path)-1):
        d+=((path[i][0]-path[i+1][0])**2+(path[i][1]-path[i+1][1])**2)**0.5
    if d<m:
        m=d
        best=path

print("Shortest Distance:",round(m,2))
print("Shortest Path:",best)
