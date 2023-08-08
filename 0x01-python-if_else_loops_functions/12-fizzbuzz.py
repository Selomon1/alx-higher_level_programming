#!/usr/bin/python3
def fizzbuzz():
    for mul in range(1, 101):
        if (mul % 3 == 0 and  mul % 5 == 0):
            print("FizzBuzz ", end="")
        elif (mul % 3 == 0):
            print("Fizz ", end="")
        elif (mul % 5 == 0):
            print("Buzz ", end ="")
        else:
            print("{} ".format(mul), end="")
