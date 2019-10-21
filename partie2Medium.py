#exo1 echec et echec
ligne2 = "# "
ligne1 = " #"
plateau = ""

for i in range(0, 8) :
    if (i % 2 == 0) :
        plateau += ligne1 * 8 + "\n"
    else :
        plateau += ligne2 * 8 + "\n"

print(plateau)

#exo2 matrix
space = ""

for i in range(1, 5) :
    for j in range(1, 5) :
        if i == j :
            space += "1 \n"
        else :
            space +=  "0 \n"
    space += "-------- \n"
    
print(space)

