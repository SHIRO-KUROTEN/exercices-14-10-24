# Exercice 1 : Compter les Voyelles

# Demandez à l'utilisateur d'entrer une phrase.
# Utilisez une boucle for pour parcourir chaque caractère de la phrase
# et comptez le nombre de voyelles (a, e, i, o, u).
# Affichez le nombre total de voyelles trouvées.
xer = input("entrer une phrase :")
voyelles =["a","e", "i", "o", "u","y"]
nb2 = 0 
for ib in voyelles :
    for ia in xer :
        if ia == ib:
            ia = 1 
            nb2 = ia + nb2
        else: 
            ia = 0    
print(nb2)
