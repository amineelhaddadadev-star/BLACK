class Gestion_des_etudiants : 
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
                    return "La note est ", self.note, " donc Reussi"
                else : 
                    return "La note est ", self.note, " Echoue"

    def ajouter_note (self,points):
        self.note = self.note + points

    def comparer_notes(self,etudiant):
        if self.note > etudiant.note : 
            print(self.nom, "a une note supérieure")
        elif self.note  < etudiant.note : 
            print(etudiant.nom, "a une note supérieure")
        else:
           print("Les deux étudiants ont la même note")      



etudiant1 = Gestion_des_etudiants("Amine",20,14)
etudiant2 = Gestion_des_etudiants("Ahmed",21,8)

etudiant1.afficher_infos()
etudiant2.afficher_infos()

resultat1 = etudiant1.verfier_resulat()
resultat2 = etudiant2.verfier_resulat()

print(resultat1)
print(resultat2)

etudiant1.ajouter_note(3)
etudiant1.ajouter_note(4)

etudiant1.comparer_notes(etudiant2)
etudiant2.comparer_notes(etudiant1)




