#Simpson's approximation of integral
#David Martínek, 2022

from cmath import inf
from math import e

#Function that is solved (e**x can be substituted with any other continuous and differentiable function)
def F(x):
    value = float(e**x)
    return value

#Pre-definitioned variables in case of reverse input 
c = 0
d = inf

#User-selected inputs
try:
    a = int(input("Zvolte dolní mez integrálu a: "))
    b = int(input("Zvolte horní mez integrálu b: "))
    if a > b:
        c = a
        d = b
        a = d
        b = c

    n = int(input("Zvolte počet podintervalů n: "))
    while n <= 0:
        n = int(input("Parametr n musí být kladný. Zadejte novou hodnotu: "))
        
except ValueError:
    print("Hodnoty musí být zadány v podobě celého čísla.")
    quit()

#Initial variables and calculation of h from inputs
sum = 0
h = (b - a)/n

#Cycle used to calculate and sumarize every subinterval of function within borders
for i in range(n+1):
    if i % 2 == 0:
        k = 4
    else:
        k = 2
    if i == 0 or i == n:
        k = 1
    x = h*(i)
    step_i_result= k*F(x)
    sum += step_i_result

#Correction for inverted inputs
if c > d:
    h = -h

#Presenting the result of an approximation
result = (h/3)*sum
print(result)