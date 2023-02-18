#here i've created a simple calculator but now i used function creation to do the opperations
#

def main():

    x1 = int(input("enter first number: "))
    x2 = int(input("enter second number: "))
    print("1. add")
    print("2. sub")
    print("3. mult")
    print("4. div")
    opera = str(input("enter the operator: "))

    if opera=="1":
        print(addition(x1, x2))
    elif opera=="2":
        print(substraction(x1, x2))
    elif opera=="3":
        print(multiplication(x1, x2))
    elif opera=="4":
        while x2==0:
            print("error, cannot divide by zero")
            x2 = int(input("enter second number: "))
        else:
            print(division(x1, x2))



def addition(n1, n2):
    return n1 + n2
def substraction(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2


main()
