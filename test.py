# declaration des variables
nom = input("votre nom").upper()
prenom = input("votre prenom").upper()

# start prg
maj = nom[0] + nom[-1]
min = prenom[0] + prenom[-1]
print(maj + min)
# end prg

# start prg age
age = float(input("age du visiteur"))
total = age/33
print(round(total))
# end prg age
