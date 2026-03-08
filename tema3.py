A = [["","",""], #tabla
["","",""],
["","",""]]
linii = len(A)
coloane = len(A[0])
contor = 0
castig = False

def afiseaza(tabla):
for i in range(len(tabla)):
print("|" ,end = " " )
for j in range(len(tabla[0])):
if A[i][j] == "" :
print("_" , end = " ")
else:
print(A[i][j], end = " ")
print("|" ,end = " " )
print()
print(afiseaza(A))

def citeste_mutare(tabla, jucator):
linii,coloane = input(f"muta {jucator}").split()
linii = int(linii)
coloane = int(coloane)
while A[linii] [coloane] != "":
print("casuta invalida/ocupata")
linii, coloane = input("alege alta valoare").split()
linii = int(linii)
coloane = int(coloane)
return linii,coloane
citeste_mutare( A , "CATALIN" )

def stare_joc(tabla):
# linii
for i in range(3):
if tabla[i][0] == tabla[i][1] == tabla[i][2] != "":
return tabla[i][0]

# coloane
for j in range(3):
if tabla[0][j] == tabla[1][j] == tabla[2][j] != "":
return tabla[0][j]

# diagonale
if tabla[0][0] == tabla[1][1] == tabla[2][2] != "":
return tabla[0][0]

if tabla[0][2] == tabla[1][1] == tabla[2][0] != "":
return tabla[0][2]
plin = True
for i in range(3):
for j in range(3):
if tabla[i][j] == "":
plin = False

if plin:
return "EGAL"

return "CONTINUA"

jucator = "X"

while True:
afiseaza(A)

linie, coloana = citeste_mutare(A, jucator)
A[linie][coloana] = jucator

stare = stare_joc(A)
if stare != "CONTINUA":
afiseaza(A)
if stare == "EGAL":
print("Joc terminat! EGAL!")
else:
print(f"Jucatorul {stare} a castigat!")
break

if jucator == "X":
jucator = "O"
else:
jucator = "X"



