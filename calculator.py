from os import system
from math import sin, cos, tan
from platform import platform
from time import sleep

def welcome():
    print("""
Welcome to calculator app

Here are the options
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Square
6. Square Root
7. Sine
8. Cosine
9. Tangent
0. Exit

Enter number of choice
 
          """)

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def square(x):
    return x ** 2

def square_root(x):
    return x ** 0.5

def sine(x):
    return sin(x)

def cosine(x):
    return cos(x)

def tangent(x):
    return tan(x)

def os_type():
    os = platform()
    if "windows" in os or "Windows" in os:
        cmd = "cls"
    else:
        cmd = "clear"
    return cmd

command = os_type()

def finish():
    system(command)
    print("Thank you for using me")
    sleep(3)
    system(command)
    exit()
    
def calculator():
    while True:
        system(command)
        welcome()
        try:
            choice = (input("Enter choice number : "))
            choice = int(choice)
        except:
            print("\nInvalid choice entered")
            sleep(3)
            continue
        else:
            if choice in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if choice in [1, 2, 3, 4]:
                    try:
                        x = int(input("\nEnter first number : "))
                        y = int(input("Enter second number : "))
                    except:
                        print("\nValue entered not integer")
                        sleep(3)
                        continue
                    else:
                        if choice == 1:
                            print("\n%i + %i = %i\n\n" % (x, y, addition(x, y)))
                        elif choice == 2:
                            print("\n%i - %i = %i\n\n" % (x, y, subtraction(x,y)))
                        elif choice == 3:
                            print("\n%i x %i = %i\n\n" % (x, y, multiplication(x,y)))
                        elif choice == 4:
                            print("\n%i / %i = %i\n\n" % (x, y, division(x,y)))
                elif choice in [5, 6]:
                    try:
                        x = int(input("\nEnter the number : "))
                    except:
                        print("\nValue entered not integer")
                        sleep(3)
                        continue
                    else:
                        if choice == 5:
                            print("\nThe square of %i is %i\n\n" % (x, square(x)))
                        elif choice == 6:
                            print("\nThe square root of %i is %f\n\n" % (x, square_root(x)))
                elif choice in [7, 8, 9]:
                    try:
                        x = float(input("\nEnter the angle : "))
                    except:
                        print("\nInvalid data entered")
                        sleep(3)
                        continue
                    else:
                        if choice == 7:
                            print("\nThe sine of %f is %f\n\n" % (x, sine(x)))
                        elif choice == 8:
                            print("\nThe cosine of %f is %f\n\n" % (x, cosine(x)))
                        elif choice == 9:
                            print("\nThe tangent of %f is %f\n\n" % (x, tangent(x)))
                else:
                    finish()
            else:
                print("\nInvalid choice entered")
                sleep(3)
                continue
            
if __name__ == '__main__':
    calculator()