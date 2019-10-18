import math

age = int(input("votre age"))
if age <= 0 :
    print("erreur")
if age >= 21 :
    print("ok")
if age%2 == 0:
    print("age pair")
else:
    print("pas pair")
if math.sqrt(age).is_integer():
    print("age carré")


