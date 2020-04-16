#Definiu la variable que ens guardarà l'estadística per noms.
noms = {}
vegades = 0
#Pista clau ha de ser el nom i valor els cops que apareix. 

#Heu de llegir el fitxer noms.
#Aneu llegint  línia a lína que correspon a un nom.
fitxer = open("noms.txt","r")
#Sumeu cap cop que apareix un nom al seu valor.
for linia in fitxer:
  if(linia not in noms):
    noms[linia] =  1 
  else:
    vegades = noms[linia]
    noms[linia] = vegades + 1


#Finalment pinteu tots els noms i amb els cops que s'ha posat el darrer any.
print(noms)
#Pintar només la variable. Els diccionaris ja surten ordenats alfabèticament.

#noms { "javi":3,"maria":4,"pepe":5}

#noms = {}

#linia -> "javi"

#si extsteix diccionari
#vegades = noms[linia]
#moms[linia] = vegades + 1

