class Etudiant :
    def __init__(self,nom,age,note):
        self.nom = nom
        self.age = age
        self.note = note
    def __str__(self):
        return f"Nom : {self.nom}  Age :{self.age}  Note : {self.note}"
    def afficher_ruslt(self) :
        print(self.nom)
        print(self.age)
        print(self.note)

etudiant1 = Etudiant("Amine", 20, 15)
etudiant2 = Etudiant("Ahmed", 21, 12)


print(etudiant1)
print(etudiant2)        