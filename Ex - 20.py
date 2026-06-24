a = [64,25,12,22,11]

for i in range(len(a)):
    swap = False

    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swap = True

    if not swap:
        break

print(a)
