import math, random #import de la librairie math et random de python

#ex1 Nombre le plus grand

#variable declaration
number1 = 1
number2 = 2
number3 = 3
number4 = 4

#function prg
def nombreLePlusGrand(n1, n2, n3, n4):
    if n1 > n2 and n1 > n3 and n1 > n4 :
        print("{} est le plus grand".format(n1))
    elif n2 > n1 and n2 > n3 and n2 > n4 :
        print("{} est le plus grand".format(n2))
    elif n3 > n1 and n3 > n2 and n3 > n4 :
        print("{} est le plus grand".format(n3))
    else :
        print("{} est le plus grand".format(n4))

a = random.randint(1, 101)
b = random.randint(1, 101)
c = random.randint(1, 101)
d = random.randint(1, 101)

numberList = [a, b, c, d]
print(max(numberList))

#dsiplay function
nombreLePlusGrand(number1, number2, number3, number4)

#ex2 Condition d'age

#variable declaration
userAge = input("votre age")

#prg if/elif/else
if len(userAge) > 0 : #check if the age is greater than 0
    userAge = int(userAge) #int convertion
    if userAge > 0 :
        if userAge >= 21 :
            print("c'est bon")
        if userAge %2 == 0 :
            print("age paire")
        if math.sqrt(userAge).is_integer() :
            print("votre age est un carré")
    else:
        print("age doit etre sup à 0") #userAge must > 0
else:
    print("vous n'avez rien mis") #userAge < 0 end of prg

#Nombre caché
nbCache = 3
userNumber = None

while userNumber != nbCache : # tant que nbCache n'est pas egal à userName
    userAge = int(input("votre nombre")) #declaration and conversion
    if userAge > nbCache :
        print("trop grand")
    elif userAge < nbCache :
        print("trop petit")
    else :
        break
print("c'est bien ça")

#Les boucles
for i in range(1, 101) :
    print(i)

for i in range(2, 101, 2) :
    print(i) #display loops 2-)100 with 2/2

for i in range(1, 101) :
    print(i%2 == 0) #display True if %2 == 0 else False

for i in range(1, 101) :
    if i%2 == 0 : #display loop with %2
        print(i)

#exo6 la piscine
def remplirPiscine(long, larg, prof, debit) : #define function for "remplir la piscine"
    tempsremplir = float((long*larg*prof)/debit)
    print("il faut {} minutes pour remplir la piscine".format(tempsremplir))

remplirPiscine(5, 2, 2, 10)

#exo7 cercle
def perimetre(rayon) : #define function for "perimetre du cercle"
    totalPerimetre = round((2 * math.pi * rayon),2)
    print("le perimetre est de {} cm".format(totalPerimetre))

def aire(rayon) : #define function for "l'air du cercle"
    totalAire = round((math.sqrt(rayon) * math.pi),2)
    print("l'air du cercle est de {} cm carrés".format(totalAire))

perimetre(5)
aire(5)

#exo8 pyramide de *
var = "\n"
espace = ""
for i in range(1, 6) :
    espace += "*"
    var += espace + "\n"

print(var)

# 9\.Exercice 9 : FIZZ BUZZ
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)







