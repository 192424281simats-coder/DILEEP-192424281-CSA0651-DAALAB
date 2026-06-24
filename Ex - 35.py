c=0

def ms(a):
    global c
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]

        ms(l)
        ms(r)

        i=j=k=0
        while i<len(l) and j<len(r):
            c+=1
            if l[i]<r[j]:
                a[k]=l[i]; i+=1
            else:
                a[k]=r[j]; j+=1
            k+=1

        a[k:]=l[i:]+r[j:]

a=[12,4,78,23,45,67,89,1]
ms(a)

print("Sorted:",a)
print("Comparisons:",c)
