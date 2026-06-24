def ms(a):
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]

        ms(l)
        ms(r)

        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]; i+=1
            else:
                a[k]=r[j]; j+=1
            k+=1

        a[k:]=l[i:]+r[j:]

a=[31,23,35,27,11,21,15,28]
ms(a)
print(a)
