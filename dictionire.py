etudiant = {
    "nom": "Amine",
    "age": 20,
    "ville": "Sale",
    "note": 15
}
etudiant ["age"] = 21
etudiant ["note"] = 17
etudiant["email"] = "amine@gmail.com"
etudiant["filiere"] = "genie logiciel"
del etudiant["ville"]


print(etudiant["age"])
print(etudiant["note"])
print (etudiant)
print(len(etudiant))
print("nom" in etudiant)
print("email" in etudiant)