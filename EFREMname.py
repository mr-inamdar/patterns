from colorama import Style,Fore,Back
def resetcoloure():
    print(Style.RESET_ALL,end="")
def resetcolour():
    print(Style.RESET_ALL)
def pl(n):
    for i in range(n):
        print(Back.RED + Fore.YELLOW + Style.BRIGHT + '*',end="")
        resetcoloure()
    print()
def E(n):
#E
    e = 1
    while(e<=n):
        if e == 1 or e == n//2 or e == n:
            pl(n)
        else:
            print(Back.RED + Fore.YELLOW + Style.BRIGHT + '*',end ="")
            resetcolour()
        e += 1
def F(n):
#F
    f = 1
    while f<=n:
        if f ==1 or f == (n//2)+1:
            pl(n)
        else:
            print(Back.RED + Fore.YELLOW + Style.BRIGHT + '*',end ="")
            resetcolour()
        f += 1
def R(n):
#R
    rx = 1
    while rx<= (n//2):
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + '*',end="")
        resetcoloure()
        for rx in range(1,rx+1):
            print(' ',end="")
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + '*',end ="")
        resetcolour()
        rx += 1
    rx = n//2
    while rx>0:
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + '*',end="")
        resetcoloure()
        for rx in range(1,rx+1):
            print(' ',end="")
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + '*',end ="")
        resetcolour()
        rx -= 1
    r = n//2
    v = 1
    while r <= n:
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + '*',end="")
        resetcoloure()
        for i in range(n//2,r+1):
            print(' ',end="")
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + '*',end ="")
        resetcolour()
        r += 1
def M(n):
#M
    for m1 in range(n):
        print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + '* ',end="")
        resetcoloure()
    print()
    for i in range(1,(n//2)+1):
        m = 1
        while m <= n:
            if m == 1 or m == n//2 or m == n:
                print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + '* ',end="")
                resetcoloure()
            else:
                print('  ',end="")
            m += 1
        print()

n = int(input("Enter a size of pattern : "))
print("--------IT'S MY NEW NAME--------")
E(n)
print()
F(n)
print()
R(n)
print()
E(n)
print()
M(n)
print("----------||  EFREM  ||----------")