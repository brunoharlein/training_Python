import math
age = int(input("votre age"))
if age <= 0:
    print("negatif")
elif age >= 21:
    print("ok")
if age %2 == 0:
    print("age pair")
if math.sqrt(age).is_integer():
    print('carré')
