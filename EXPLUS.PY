notes = {
    "Amine": 15,
    "Ahmed": 8,
    "Yassine": 17,
    "Omar": 11,
    "Hamza": 7,
    "Said": 14
}
compteur = 0

class Etudiant : 

    def __init__(self, nom, note):
        self.nom = nom
        self.note = note    

    def __str__(self):
            return f"Nom : {self.nom}  Note : {self.note}"    

    def verifier_note(self):
        if self.note >= 10:
          return "Réussi"
        else:
          return "Échoué"
          
    def ajouter_note(self,points):
        self.note = self.note + points 

etudiant1 = Etudiant("Amine", 15)

etudiant1.ajouter_note(2)

print(etudiant1)
print(etudiant1.verifier_note())

etudiants = []

for nom, note in notes.items():
    etudiant = Etudiant(nom, note)
    etudiants.append(etudiant) 
for etudiant in etudiants:
    print(etudiant)
    print(etudiant.verifier_note())
