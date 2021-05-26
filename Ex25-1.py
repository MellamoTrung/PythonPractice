import math
amount_seconds = float(input("Insert number of seconds: "))
day = int(amount_seconds // 86400)
hour = int((amount_seconds - day*86400)/3600)
minute = int((amount_seconds - hour*3600 - day*86400)/60)
second = int(amount_seconds - minute*60 - hour*3600 - day*86400)
print("{:02d} : {:02d} : {:02d} : {:02d}".format(day, hour, minute, second))
