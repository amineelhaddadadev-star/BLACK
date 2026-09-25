notes = {
    "Amine": 15,
    "Ahmed": 9,
    "Yassine": 17,
    "Omar": 11,
    "Hamza": 7,
    "Said": 14,
    "Karim": 20,
    "Mehdi": 12,
    "Anas": 6,
    "Reda": 18
}
somme_naj7in = 0
somme_sa0tin = 0
naj7 = 0
sa9t = 0
mailleure = 0
nom_meilleur = ""
for nom,note in notes.items():
    if note >= 10 :
       najh = naj7 + 1
    elif note <  10 :
        sa9t = sa9t + 1
    if note  >= 10 :
        somme_naj7in = somme_naj7in+ note
    elif note < 10 :
        somme_sa0tin = somme_sa0tin + note
    if note > mailleure:
        mailleure = note
        nom_meilleur = nom
        

print("Reussis :", naj7)
print("Echoues :", sa9t)
print("Somme des réussis :", somme_naj7in)
print("Somme des Echoues :", somme_sa0tin)
print("Meilleure note :", mailleure) 
print("meilleur etuditnt", ":" , nom_meilleur)          
