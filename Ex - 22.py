id="6zjlwm"
arr = [2,3,4,7,11]
k = 5
num = 1

while k:
    if num not in arr:
        k -= 1
    if k == 0:
        print(num)
    num += 1
