def signe (a , b) :
    if a == 0 or b == 0 :
     print("au moins un nombre est zero")
    if a*b > 0 :
         print("a et b sont le meme signe")
    else :
         print("a et b esst differnte")

def minimue (a,b) : 
     if a>b :
      return b
     else :
      return a

def maximue (a,b) :
    if b>a :
      return b
    else :
      return a
    
a = int(input("entre la nombre de a :"))
b = int(input("entre le nombre de b :")) 
signe(a,b)
min = minimue(a,b)
print("la valeur manimal est :" ,min)
print("la valeur maximal est :",maximue(a,b))