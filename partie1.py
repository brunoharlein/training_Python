# ex 1 afficher "hello world"
print("hello world")
variable = "hello world"
print(variable)

# ex 2 calcul
print(3*3, 4+9+78, 12-7, 5e4)
try:
    12/0
except ZeroDivisionError:
    print("pas possible de diviser par 0")

# ex3 Bonjour ordi
nom = input("votre nom")
print("Bonjour {}".format(nom))

# ex4 nom et prenom
nom = "harlein"
prenom = "bruno"

print("bonjour {} {}".format(prenom, nom))

#exo5 chiffre
my_number = "123"
print(int(my_number))

#exo6 Maj et Min
texte = input("votre texte")
maj = texte.upper()
print(maj)

min = texte.lower()
print(min)






