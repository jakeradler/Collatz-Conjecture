from __future__ import division
import math

n= int((input("Please Enter any Number: ")))
steps = 0;

first_digit = n

while (first_digit >= 10):
    first_digit = first_digit // 10

while n!=1:
   if n%2==0:
       n=n/2
       steps += 1
   if n%2!=0 and n!=1:
       n=3*n+1
       steps += 1
   print(math.trunc(n))
   
print("It took " + str(steps) + " steps to reach the Collatz conjecture")
print("The First Digit from a Given Number {0} = {1}".format(n, first_digit))
