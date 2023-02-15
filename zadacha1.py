
n = int(input())
w = input().split()
mx = 0
mn = 0
for i in range(n):
    for j in range(1, n - 1):
        if int(w[i]) > int(w[j]):
            mx = w[i]
for i in range(n):
    for j in range(1, n - 1):
        if int(w[i]) > int(w[j]):
            w[i] = 0
        for k in w:
            if int(k) != 0:
                mn = int(k)
print(mn, mx)