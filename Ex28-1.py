print("Hello, welcome to the BMI compute program")
a = input("If you want to compute BMI in (inch, pound) --> Type \"1\"\nIf you want to compute BMI in (meter, kilogram) --> Type \"2\"\n --> ")
if a == '1':
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    BMI = (weight*703)/(height**2)
elif a == '2':
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    BMI = (weight)/(height**2)
print("Your BMI : {}".format(BMI))
