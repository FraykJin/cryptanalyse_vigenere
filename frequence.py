#import sys

#fichier = sys.argv[1]

def frequence(fichier):
    letters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    listFreq = []
    
    for i in range(0,26):
        listFreq.append(0)
    
    file = open(fichier, "r")
    ligne = file.read()
    
    for i in range(0,26):
        
        for lettre in ligne:
            if letters[i] == lettre:
                listFreq[i] += 1
    
    for j in range(0,26):
        listFreq[j] = listFreq[j]/len(ligne)
        
        
    return listFreq

#frequence(fichier)