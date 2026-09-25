produits = {
    "Laptop": 8000,
    "Telephone": 4000,
    "Clavier": 300,
    "Souris": 150,
    "Ecran": 2000
}
class Produit :
    def __init__(self,nom,prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Nom : {self.nom} Prix : {self.prix} DH" 

    def est_cher(self):
        if self.prix >= 2000:
           return "Cher"
        else :
           return "Pas cher"

    def ajouter_reduction(self,pourcentage):
        reduction = self.prix * pourcentage / 100
        self.prix = self.prix - reduction


produit1 = Produit("Laptop", 8000)
produit1.ajouter_reduction(10)
print(produit1)

liste_produits = []
for nom,prix in produits.items():
    produit = Produit(nom,prix)
    liste_produits.append(produit)

for produit in liste_produits:
    print(produit)    

for produit in liste_produits:
    print(produit.nom, ":", produit.est_cher())

for produit in liste_produits:
    if produit.prix >= 2000:
        reduction = produit.prix * 10 / 100
        produit.prix = produit.prix - reduction
        print(produit)
somme = 0 

for produit in liste_produits:
    somme = somme + produit.prix 
print(somme)

maximun_produits = 0
nom_maximum = "" 

for produit in liste_produits:
    if produit.prix > maximun_produits :
     maximun_produits = produit.prix
     nom_maximum = produit.nom
print("Produits le plus cher",nom_maximum)     
print(maximun_produits)
