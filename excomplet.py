nombres = [12, 5, 18, 7, 21, 30, 9, 14, 25, 8] 

def analyser(liste):
   somme = 0 
   immpaier = 0
   paire = 0 
   immpaier_fo9_10 = 0
   for i in liste:
        if i % 2 == 0 : 
            paire = paire + 1
        else : 
            immpaier = immpaier + 1
        if i % 2 == 0 :
            somme = somme + i  
        elif i % 2 != 0 and i > 10 : 
            immpaier_fo9_10 = immpaier_fo9_10 + i

   return paire, immpaier, somme, immpaier_fo9_10

result = analyser(nombres)
print(result)                   
