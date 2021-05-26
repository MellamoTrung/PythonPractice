feet_value = float(input("Insert the value in feet: "))
inch_value = feet_value*12
yard_value = feet_value*1/3
mile_value = feet_value*0.0001893939
print("The converted result {} feet equal:\n+ {} inch\n+ {} yard\n+ {}".format(feet_value, inch_value, yard_value, mile_value))
