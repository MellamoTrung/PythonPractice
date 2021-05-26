def area(length, width):
    area_in_arce = (length*width)/43560
    return(area_in_arce)
a = float(input("Enter the length : "))
b = float(input("Enter the width  : "))
print("The area in arces: {}".format(area(a, b)))