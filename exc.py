nombres = [8, 15, 22, 7, 30, 11, 18, 5, 40]
def analyser(liste):
  somme_kbar_10  = 0   
  somme_sgharmn10wlatsawi=0
  compteur = 0
  for i in liste:
    if i > 10 :
      somme_kbar_10 = somme_kbar_10 + 1
    elif i <= 10 :
      somme_sgharmn10wlatsawi = somme_sgharmn10wlatsawi + 1
    if i > 10 :
      compteur = compteur + i
  return somme_sgharmn10wlatsawi,somme_kbar_10,compteur
resultat = analyser(nombres)
print(resultat)
      
