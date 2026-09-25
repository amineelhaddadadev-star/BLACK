class Etudiant : 
    def __init__(self,nom,age,note):
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_infos(self):
        print("Nom :" , self.nom)
        print("Age : ", self.age)
        print("Note : ", self.note)

    def verfier_resultat(self,):
        if self.note >= 10 : 
            return'Reussi'
        else : 
            return 'Echoue'
    def ajouter_note(self,points):
        self.note = self.note + points

etudiant1 = Etudiant("Amine", 20, 15)
etudiant2 = Etudiant("Ahmed", 21, 8)

etudiant1.afficher_infos()
etudiant2.afficher_infos()


resultat1 = etudiant1.verfier_resultat()
resultat2 = etudiant2.verfier_resultat()

print(resultat1)
print(resultat2)

etudiant1.ajouter_note(3)