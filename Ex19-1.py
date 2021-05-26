import math
vi = float(input("Enter the initial speed   : "))
d = float(input("Enter the distance         : "))
vf = math.sqrt((vi**2) + 2*9.8*d)
print("The final speed is {}".format(vf))