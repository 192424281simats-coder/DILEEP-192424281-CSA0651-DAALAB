p=[(1,2),(4,5),(7,8),(3,1)]
m=999
for i in range(len(p)):
    for j in range(i+1,len(p)):
        d=((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)**0.5
        if d<m:
            m=d
            c=(p[i],p[j])
print("Closest Pair:",c)
print("Minimum Distance:",m)
