nombres = [12, 5, 18, 21, 30, 7, 44, 9, 16, 25]
def analyser(liste):
    paire = 0
    impaire = 0
    somme_paire = 0
    somme_impaire = 0
    for i in liste : 
        if i % 2 == 0 : 
            paire = paire + 1
        elif i % 2 != 0  :
            impaire = impaire + 1
        if i % 2 == 0 : 
            somme_paire = somme_paire + i
        if i % 2 != 0 and i > 20:
            somme_impaire = somme_impaire + i        
        
    return paire ,impaire, somme_paire, somme_impaire        
ruslt = analyser(nombres)
print(ruslt)  