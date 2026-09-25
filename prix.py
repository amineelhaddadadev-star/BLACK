def calcul_prix(prix, quantité):
    total = prix * quantité
    if total >= 1000 : 
        return total * 0.70
    elif total >= 500 :
        return total * 0.80
    elif total >= 100 :
        return total * 0.90
    else :
        return total
         
        

prix = float(input("entre le prix :"))
quantité = int(input("entrer qunatit : "))    
resulat = calcul_prix(prix,quantité)

print("le prix final est :",resulat)