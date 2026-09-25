class Etudiant :
    def __init__(self,nom,age,note):
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_infos(self):
        print("Nom :" , self.nom)
        print("Age : ", self.age)
        print("Note : ", self.note)

    def verfier_resulat(self):
        if self.note >= 10 : 
            print("La note est ", self.note, " donc Reussi")
        else : 
            print("La note est ", self.note, " Echoue")

    def ajouter_note(self,points):
        self.note = self.note + points

Etudiant1=Etudiant("Amine",20,12)

Etudiant1.afficher_infos()
Etudiant1.verfier_resulat()
Etudiant1.ajouter_note(5)
Etudiant1.afficher_infos()
Etudiant1.verfier_resulat()
Etudiant1.ajouter_note(10)
Etudiant1.verfier_resulat()

                    



