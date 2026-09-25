nombres = [12, 5, 18, 7, 25, 30, 9, 14, 21, 8]
def analyser(liste):
    nombres_pair = 0
    nombres_impaire = 0
    compteur_pair = 0
    commpteur_impaire  = 0

    for i in nombres :
        if i % 2 == 0 :
         nombres_pair = nombres_pair + 1
        elif  i % 2 != 0 :
           nombres_impaire = nombres_impaire + 1
        if  i % 2 == 0 :
           compteur_pair = compteur_pair + i
        elif  i % 2 != 0 :
           commpteur_impaire = commpteur_impaire + i
    return commpteur_impaire,compteur_pair,nombres_impaire,nombres_pair
resultat = analyser(nombres)
print(analyser)          