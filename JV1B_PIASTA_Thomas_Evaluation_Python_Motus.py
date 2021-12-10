# D'abord j'importe colorama et mon module random pour choisir les mots au hasard
from colorama import init
from colorama.ansi import Fore
init()
import random

# Ensuite je crée ma liste de mots et et j'utilise une fonction random pour en selectionner un au hasard
liste = ['depart', 'climat', 'python', 'dindon', 'violet', 'casque', 'source', 'maison', 'numero', 'accent']
def selectRandom(liste):
    return random.choice(liste)

# Ensuite je crée mes variables
mot = selectRandom(liste)
motcache = ""
reponse = ""
tour = 0
victoire = False

# Ensuite je code le programme qui va me permettre d'afficher le mot caché par des '*'
for i in range (len(mot)):
    motcache = motcache + "*" 
print(motcache + "\nDevinez le mot")

# Ici je commence mon programme principal
while victoire != True:
        tentative = input("\nEntrez un mot ")
        tour = tour + 1
        for i in range (len(tentative)):
            if tentative[i] == mot[i]:
                print(Fore.RED + mot[i])
                if tentative == mot: 
                    print()
                    victoire = True
            elif tentative[i] in mot:
                print(Fore.YELLOW + tentative[i])
            else:
                print (Fore.BLUE + tentative [i])
        if tour == 8: 
            print("Défaite")
            victoire = True

print("Gagné !")

            
                    

                
        
    

    


