"""
Name: generate_pi_500.py
Purpose: Get the value of Pi to n number of decimal digits (up to 500 digits after the dot)
Author: tan_4ik_444
Algorithm: Chudnovsky Algorithm
License: MIT
Module Dependencies:
Decimal is required for the Decimal data type which is much better than Float for big calculation
"""

import decimal
from decimal import Decimal, getcontext, ROUND_HALF_UP #use ROUND_HALF_UP for mathematical rounding rule
 
def factorial(k): #function for factorial calculation
    a=Decimal(1)
    for i in range (int(k)):
        if i ==0:
            a*=Decimal(1)
        else:
            a*=Decimal(i)
    #print (type(a))
    return Decimal(a)
          
def amount_calculation(k): #function for calculation the amount from the Chudnovsky Algorithm
    i=k+1
    amount = Decimal(0)
    for i in range (k):
        top = (Decimal(-1))**Decimal(i)*factorial(Decimal(6)*Decimal(i))*(Decimal(13591409)+Decimal(54514013)*Decimal(i))
        bottom = factorial(Decimal(3)*Decimal(i))*((factorial(i))**Decimal(3))*(Decimal(640320)**(Decimal(3)*Decimal(i)+Decimal(1.5)))
        amount += top/bottom
    return Decimal(amount)
 
def start():  #the function of running the main calculation
    while True:
        print ("Welcome to Pi Calculator. Please enter the number of digits up to which the value of Pi should be calculated or enter quit to exit")
        entry = input()
        if entry == "quit":
            print ("Thank you! Bye!")
        elif not entry.isdigit():
            print ("You did not enter a number. Try again")
        elif entry.isdigit():
            if int(entry)>500:  #to set up the limit for calculation - 500 digits after the dot
                getcontext().prec = 500+1  
                print ('limit is 500')
            else:
                getcontext().prec = int(entry)+1
            x=amount_calculation(int(entry))
            pi=1/(Decimal(12)*x)  #the last calculation from the Chudnovsky Algorithm 
            print (pi)
            return
      
if __name__=='__main__':
    start()
