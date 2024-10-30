# Exercice 3 : Table de Multiplication

# Demandez à l'utilisateur d'entrer un nombre entier.
# Utilisez une boucle for pour afficher la table de multiplication de ce nombre de 1 à 10.
x = int(input(" entrer un nombre :"))
print( "la table de",x,":")
for i in range (11):

    print(x,"*",i,"=", x*i)
