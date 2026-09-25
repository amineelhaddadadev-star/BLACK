def calcul_mention(note):
    if note > 20 or note < 0 :
        return"Note invalider"
    if  note < 10 :
        return "Echec"
    elif note < 12 :
        return "Passable"
    elif note < 14 : 
        return " Assez bien"
    elif note < 16  :
        return "bien"
    else :
        return "tres bien"

        
note = float(input("Entre la note :"))
resultat = calcul_mention(note)
print(resultat)
