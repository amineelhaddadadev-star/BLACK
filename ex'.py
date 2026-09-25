notes = {
    "Amine": 15,
    "Ahmed": 8,
    "Yassine": 17,
    "Omar": 11,
    "Hamza": 7,
    "Said": 14
}
def analyser(notes):

    naj7 = 0
    sa9t = 0
    somme  = 0 
    mailler_note = 0 

    for nom,note in notes.items():
        if note >= 10 :
            naj7 = naj7 + 1
        elif note < 10  :
            sa9t = sa9t + 1
        if note >= 10 : 
            somme = somme + note
        if note > mailler_note : 
            mailler_note = note    
    return naj7,sa9t,somme ,mailler_note           
resultat = analyser(notes)
print(resultat)

