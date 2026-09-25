employes = {
    "Amine": 6500,
    "Ahmed": 4200,
    "Yassine": 8000,
    "Omar": 3500,
    "Hamza": 7200
}
class Employe : 
    def __init__(self,nom,salaire):
        self.nom = nom
        self.salaire = salaire

    def __str__(self):
        return f"Nom :  {self.nom} | Salaire :{self.salaire} DH"     

    def est_bien_paye(self):
        if self.salaire >= 6000 : 
            return "bien paye"
        else : 
            return "Salaire normal"

    def augmenter(self, pourcentage):
        augmentation = self.salaire * pourcentage / 100
        self.salaire = self.salaire + augmentation
  
        
Employe1 = Employe("Amine",6500)      
print(Employe1)   
liste_employes = []  
for nom,salaire in employes.items():
    employe = Employe(nom,salaire)
    liste_employes.append(employe)

for employe in liste_employes:
    print(employe)        

somme = 0 
for employe in liste_employes:
    somme = somme + employe.salaire
print(somme)   

compter = 0
for employe in liste_employes:
    if employe.salaire >= 6000:
        compter = compter + 1
       
print(compter)  

for employe in liste_employes:
    if employe.salaire < 6000:
        employe.augmenter(10)
    print(employe) 