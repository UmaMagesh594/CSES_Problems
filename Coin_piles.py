for i in range(int(input())):
    A,B = map(int,input().split())
    if (A+B) % 3 == 0 and min(A,B)*2 >= max(A,B):
        print("YES")
    else:
        print("NO")
