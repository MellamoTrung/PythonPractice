import math
a = float(input("a = "))
b = float(input("b = "))
print("----> a + b = {}\n----> b - a = {}\n----> a x b = {}\n----> a // b = {}\n----> a '%' b = {}\n----> log10(a) = {}\n----> a^b = {}".format(a+b, b - a, a*b, a//b, a%b, math.log10(a), a**b))