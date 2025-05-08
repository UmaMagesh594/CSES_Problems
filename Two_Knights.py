for k in range(1, int(input()) + 1):
    print(0 if k < 2 else ((k * k * (k*k-1))//2) - (4 * (k-1)*(k-2)))
