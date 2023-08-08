#!/usr/bin/python3
def fizzbuzz():
   for mul in range(1, 101):
       if (mul % 3 == 0 and  mul % 5 == 0):
           print("fizzbuzz ", end="")
       elif (mul % 3 == 0):
           print("fizz ", end="")
       elif (mul % 5 == 0):
           print("buzz ", end ="")
       else:
           print(mul, end="")
