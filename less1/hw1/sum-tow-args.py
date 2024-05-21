import sys
import math
#2
arg1=float(sys.argv[1])
arg2=float(sys.argv[2])
print(arg1+arg2)

#3
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Current date and time =", dt_string)

#4
r=float(input("Enter radius"))
print("r= {} Area={}" .format(r,r*r*math.pi))

