chaine = input("Veuillez entrer une série de valeur séparées par un espace\n")
# chaîne contient une "string"
print(chaine)

val_str = chaine.split()
# val_str contient une liste de "string"
print(val_str)

# 'map' applique la fonction int à chaque élément de la liste
val_int = list(map(int, val_str))
# val_int contient une liste de "int"
print(val_int)