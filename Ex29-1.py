import math
temperature = float(input("Enter the air temperature: "))
speed = float(input("Enter the wind speed: "))
WCI = round(13.12 + 0.6215*temperature - 11.37*(speed**0.16) + 0.3965*temperature*(speed**0.16))
print("WCI = {}".format(WCI))
