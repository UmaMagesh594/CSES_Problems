N = int(input())
A = []
while N > 1:
    A.append(N)
    if N % 2 == 0:
        N = N // 2
    else:
        N = (N * 3) + 1
A.append(1)
print(*A)
