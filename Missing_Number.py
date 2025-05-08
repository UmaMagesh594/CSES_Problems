A = int(input())
B = [int(i) for i in input().split()]
count = 1
for i in sorted(B):
    if i != count:
        break
    count += 1
print(count)
