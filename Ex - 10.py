def sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    l = sort(a[:mid])
    r = sort(a[mid:])
    res = []

    while l and r:
        res.append(l.pop(0) if l[0] < r[0] else r.pop(0))

    return res + l + r

nums = [5, 2, 3, 1]
print(sort(nums))
