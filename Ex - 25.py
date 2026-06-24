id="gqvzxz"
words = ["mass","as","hero","superhero"]
ans = []

for i in words:
    for j in words:
        if i != j and i in j:
            ans.append(i)
            break

print(ans)
