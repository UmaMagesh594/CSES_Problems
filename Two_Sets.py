N = int(input())
total = N * (N + 1) // 2
if total % 2 != 0:
    print("NO")
else:
    A = []
    B = []
    tar = total // 2
    for i in range(N,0,-1):
        if tar >= i:
            A.append(i)
            tar -= i
        else:
            B.append(i)

    print("YES")
    print(len(A))
    print(*A)
    print(len(B))
    print(*B)
