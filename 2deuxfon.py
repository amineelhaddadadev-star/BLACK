def calcul_moyenne(note1,note2,note3):
    return (note1 + note2 + note3) / 3
def resultat(moyenne):
    if moyenne < 10 :
        return "echec"
    elif moyenne < 12 :
        return "passable"
    elif moyenne < 14 :
        return "Assez bien"
    elif moyenne < 16 :
        return"Bien"
    else :
        return"Tres bien"

note1 = float(input("donner 1 la note :"))   
note2 = float(input("donner 2 la note :"))    
note3 = float(input("donner 3 la note :"))  

moyenne = calcul_moyenne(note1,note2,note3)
print(moyenne)
res = resultat(moyenne)
print(res)


