def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n :
        print("Holy smokes, Fermat was wrong!")
    else:
        print ("No, that doesn't work.")

def ferm_input():
    print('-'*40)
    print("Welcome to Fermat Theory Checker!")
    print('-'*40)
    print("Please input the four values")

    a = (int) (input("a: "))
    b = (int) (input("b: "))
    c = (int) (input("c: "))
    n = (int) (input("n: "))

    check_fermat(a, b, c, n)

ferm_input()