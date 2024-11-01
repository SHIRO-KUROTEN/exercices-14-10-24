# Exercice 5 : Mot de Passe Correct


#  Créez une variable mot_de_passe et attribuez-lui une valeur, par exemple "python123".
#  Demandez à l'utilisateur d'entrer le mot de passe.
#  Tant que le mot de passe n'est pas correct, redemandez-le (à l'aide d'une boucle while).
#  Quand le mot de passe est correct, affichez "Accès autorisé".
mdp="python123"
x= input("entrer le mot de passe : ")

while mdp != x :
    
    print("mot de passe incorect")
    x= input("entrer le bon mot de passe : ")
print(" pimp pam poum :","","le mot de passe correct")