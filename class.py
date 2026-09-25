class etudiant : 
    def __init__(self,nom,age,email,ville,num):
        self.nom  = nom
        self.age = age
        self.email = email
        self.ville = ville
        self.num = num
etudiant1 = etudiant(
    "Amine",
    20,
    "amine@gmail.com",
    "Rabat",
    "0606060606"
)       
print(etudiant1.nom,
      etudiant1.age,
      etudiant1.email,
      etudiant1.ville,
      etudiant1.num)
