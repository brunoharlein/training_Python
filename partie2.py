#True or False (1)
var = ""
var2 = "test"

if len(var) == 0:
    print(False)
else:
    print(True)

if len(var2) == 0:
    print(False)
else:
    print(True)

#age calculation (2)
anneeEnCours = int(input("année en cours"))
DDN = int(input("Votre année de naissance"))

UserAge = anneeEnCours - DDN
print("Vous avez {}".format(UserAge))

OtherUserAge = int(input("Age du visiteur"))

totalAge = UserAge + OtherUserAge
print("La somme de vos ages est de {}".format(totalAge))

#Shoes problem (3)
prix1 = 70
prix2 = 59
prix3 = 20
total = prix1 + prix2 + prix3

print("La somme des achats avec la reduction est de {}".format(total * 0.8))

#Calculator (4)
number1 = float(input("Nombre 1"))
number2 = float(input("Nombre 2"))

print("La somme des deux est {}".format(number1 + number2))

#Name with upper and lower (5)
nom = input("votre nom").upper()
prenom = input("votre prenom").upper()

Nom = nom[0] + nom[-1]
Prenom = prenom[0] + prenom[-1]
print(Nom + Prenom)

age = float(input("age du visiteur"))
total = age/33
print(round(total))


