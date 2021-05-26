cost = input("Enter the cost: ")
cost = float(cost)
tax = 0.1*cost 
tip = 0.18*cost
total = cost + tax + tip
print("Summary: \n - Cost: {} VND\n - Tax: {} VND\n - Tip: {} VND\n    GRAND TOTAL: {} VND".format(cost, tax, tip, total))