# Exercice 7 : Compter les Caractères


#  Demandez à l'utilisateur d'entrer un mot.
#  Utilisez une boucle for pour compter combien de fois chaque caractère apparaît dans le mot.
#  Affichez le résultat sous la forme : "Le caractère 'x' apparaît y fois."

x= list(input(" entrer un mot :"))
y=0
z=x[:]
for a in (x): 
    for i in (z):
        if i == a :
            y= y + 1
            
        else:
            y = y +0    
       
    
    print("il y a ",y ,a," dans les mots")
    y =0
    
    