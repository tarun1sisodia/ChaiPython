import sys
from fractions import Fraction
from decimal import Decimal
ideal_temp = 95.5
excat_temp = 95.49

print(f"Ideal Temp: {ideal_temp}")
print(f"Current Temp :{excat_temp}")
print(f"Difference Temp :{ideal_temp -excat_temp}")
print(sys.float_info)