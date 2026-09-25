nombres = [12, 7, 25, 4, 18, 31, 10, 22, 9, 40]
def analyser(liste):
    nombres_pair = 0
    nombres_impaire = 0
    compteur_pair = 0
    commpteur_impaire  = 0
    grand_nombre = 0


    for i in liste:

        if i % 2 == 0 :
         nombres_pair = nombres_pair + 1

        elif  i % 2 != 0 :
           nombres_impaire = nombres_impaire + 1

        if  i % 2 == 0 :
           compteur_pair = compteur_pair + i

        elif  i % 2 != 0 :
           commpteur_impaire = commpteur_impaire + i

        if i > grand_nombre:
           grand_nombre  = i 
               


    return nombres_pair, nombres_impaire, compteur_pair, commpteur_impaire, grand_nombre


resultat = analyser(nombres)
print(resultat)        
      
