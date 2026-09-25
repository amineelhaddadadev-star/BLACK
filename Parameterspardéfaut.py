personne = {
    "nom": "Amine",
    "age": 20,
    "ville": "Rabat"
}

def afficher_perssone(personne) :
    print("nom : ", personne["nom"])
    print("age : ", personne["age"])
    print("ville : ", personne["ville"])

def modifier_age(personne, nouvel_age):
    personne["age"] = nouvel_age


afficher_perssone(personne) #afficher les information avant mpodification

modifier_age(personne, 25) # Modifier l'âge

print("\nAprès modification :")# Afficher les informations après modification

afficher_perssone(personne)