A = int(input())
B = [int(i) for i in input().split()]
steps = 0
for i in range(1,A):
    if B[i] < B[i-1]:
        steps += B[i-1] - B[i]
        B[i] = B[i-1]
print(steps)
