#X
n = int(input("Enter a size of Pattern : "))
#part - |
t = 0
p = (2*n)-3
for i in range(n):
    for e in range(t):
        print(" ",end="")
    print("*",end="")
    for x in range(p):
        print(" ",end="")
    if(i == n-1):
        print()
    else:
        print("*")
    t+=1
    p-=2
#part - ||
t = n-2
p=1
for m in range(n-1):
    for r in range(t):
        print(" ",end="")
    print("*",end="")
    for k in range(p):
        print(" ",end="")
    print('*')
    t-=1
    p+=2