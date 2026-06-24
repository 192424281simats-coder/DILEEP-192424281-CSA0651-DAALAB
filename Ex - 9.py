arr = sorted([3, 4, 6, -9, 10, 8, 9, 30])
key = 10

l, h = 0, len(arr)-1

while l <= h:
    m = (l+h)//2
    if arr[m] == key:
        print("Found at position", m+1)
        break
    elif arr[m] < key:
        l = m+1
    else:
        h = m-1
else:
    print("Not found")
