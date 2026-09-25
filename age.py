def calcul_age(age):
    if age < 0 :
       return " Age invalider"
    if age < 13 :
       return "Enfant"
    elif age < 18 :
       return "Adolescent"
    elif age < 60 :
       return "Adult"
    else :
       return "Senior"
    

age = int(input("Entrer age :"))    
resultat = calcul_age(age)
print(resultat) 