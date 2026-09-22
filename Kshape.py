n = int(input("Enter a size of Pattern : "))
#part - |
K = n
for ar in range(n):
    print('*',end="")
    for si in range(K):
        print(" ",end="")
    print('*')
    K-=1
#part -||
K = 0
for ar in range(n):
    print('*',end="")
    for si in range(K):
        print(" ",end="")
    print('*')
    K+=1

