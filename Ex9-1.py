money = float(input("Enter your initial amount of money: "))
input_year = int(input("Enter the year you want to check (1, 2, 3,...): "))
print("The total amount of money after {} year is {}.".format(input_year, money*((1 + 0.04)**input_year)))