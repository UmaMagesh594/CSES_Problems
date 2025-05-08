A = int(input())
if A == 2 or A == 3:
    print("NO SOLUTION")
else:
    for i in range(2,A+1,2):
        print(i,end = " ")
    for i in range(1,A+1,2):
        print(i,end = " ")
