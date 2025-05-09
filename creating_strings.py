from itertools import permutations
A = input()
B = set(permutations(A))
C = []
for i in B:
    C.append(i)
print(len(C))
for i in sorted(C):
    print(''.join(i))
