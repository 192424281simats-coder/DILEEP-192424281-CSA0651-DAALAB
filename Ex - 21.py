a = [3,1,4,1,5,9,2,6,5,3]

for i in range(1,len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j -= 1

    a[j+1] = key

print(a)
