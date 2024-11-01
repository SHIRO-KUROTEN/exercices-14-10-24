# Exercice 4 : Somme des Entiers


#  Demandez à l'utilisateur d'entrer un nombre entier positif n.
#  Utilisez une boucle for pour calculer la somme des nombres de 1 à n.
#  Affichez la somme totale.
n=int(input("entrer un nombre entier : "))
x = 0 
for i in range (n+1):
    x = i + x
print("la some de 1 a",n,"est :", x)

