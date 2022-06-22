from math import *

num1 = float(input())
num2 = float(input())

sr_arif = (num1 + num2) / 2
sr_geo = sqrt(num1 * num2)
sr_gar = (2 * num1 * num2) / (num1 + num2)
sr_kvadr = sqrt((num1 ** 2 + num2 ** 2) / 2)

print(sr_arif)
print(sr_geo)
print(sr_gar)
print(sr_kvadr)