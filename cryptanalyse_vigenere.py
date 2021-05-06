
# Sorbonne Université 3I024 2019-2020
# TME 2 : Cryptanalyse du chiffre de Vigenere
#
# Etudiant.e 1 : Jin 3520447
# Etudiant.e 2 : Mmadi Ali 3520922

import sys, getopt, string, math
#import frequence
# Alphabet français
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Fréquence moyenne des lettres en français
# À modifier
freq_FR = [0.09213414037491088, 0.010354463742221126, 0.030178915678726964, 0.03753683726285317, 0.17174710607479665, 0.010939030914707838, 0.01061497737343803, 0.010717912027723734, 0.07507240372750529, 0.003832727374391129, 6.989390105819367e-05, 0.061368115927295096, 0.026498684088462805, 0.07030818127173859, 0.049140495636714375, 0.023697844853330825, 0.010160031617459242, 0.06609294363882899, 0.07816806814528274, 0.07374314880919855, 0.06356151362232132, 0.01645048271269667, 1.14371838095226e-05, 0.004071637436190045, 0.0023001447439151006, 0.0012263202640210343]
#freq_FR = frequence.frequence("germinal.txt")



# Chiffrement César
def chiffre_cesar(txt, key):
    """
    Documentation à écrire
    """
    if key > 26 or key <= 0 :
        print("Pas de chiffrement")
        sys.exit
        
    txtCypher = ""
    
    for c in txt:
        numero = (alphabet.index(c) + key) % 26
        caracChiffre = alphabet[numero]
        txtCypher += caracChiffre

    return txtCypher

# Déchiffrement César
def dechiffre_cesar(txt, key):
    """
    Documentation à écrire
    """
    
    if key > 26 or key < 0 :
        print("Pas de chiffrement")
        sys.exit
    
    
    txtDechiffre = ""
    
    for c in txt:
        numero = (alphabet.index(c) - key) % 26
        caracChiffre = alphabet[numero]
        txtDechiffre += caracChiffre

    return txtDechiffre
    

# Chiffrement Vigenere
def chiffre_vigenere(txt, key):
    """
    Documentation à écrire
    """
    if len(key) <= 0 or len(key) > 20:
        print("Taille key incompatible")
        sys.exit
    
    txtCypher = ""
    compteur = 0
    
    for c in txt:
        numero = (alphabet.index(c) + key[compteur]) % 26
        caracChiffre = alphabet[numero]
        txtCypher += caracChiffre
        #Fin de repetition des entiers pour VIGENERE
        if compteur == len(key) - 1:
            compteur = 0
        else:
            compteur +=1
        
    return txtCypher

# Déchiffrement Vigenere
def dechiffre_vigenere(txt, key):
    """
    Documentation à écrire
    """
    if len(key) <= 0 or len(key) > 20:
        print("Taille key incompatible")
        sys.exit
    
    txtDechiffre = ""
    compteur = 0
    
    for c in txt:
        numero = (alphabet.index(c) - key[compteur]) % 26
        caracChiffre = alphabet[numero]
        txtDechiffre += caracChiffre
        
        if compteur == len(key) - 1:
            compteur = 0
        else:
            compteur +=1
        
    return txtDechiffre

# Analyse de fréquences
def freq(txt):
    """
    Documentation à écrire
    """
    
    hist=[0.0]*len(alphabet)
    
    for c in txt:
        hist[alphabet.index(c)] += 1
    
    return hist

# Renvoie l'indice dans l'alphabet
# de la lettre la plus fréquente d'un texte
def lettre_freq_max(txt):
    """
    Documentation à écrire
    """
    hist = freq(txt)
    #max renvoie l'element le plus grand dans une liste
    #on retourne la lettre ayant le plus d'occurence dans txt
    #return alphabet.index(hist.index(max(hist)))
    hist.index(max(hist))
    return alphabet.index(alphabet[hist.index(max(hist))])

# indice de coïncidence
def indice_coincidence(hist):
    """
    Documentation à écrire
    """
    indiceCoincidence = 0.0
    #Nombre total de caracteres dans le texte
    nbTotal = sum(hist)
    #Calcul de l'indice ce coincidence
    if nbTotal > 0:
        for i in hist:
            indiceCoincidence += (i*(i-1)) / (nbTotal*(nbTotal -1))
        
    return indiceCoincidence

# Recherche la longueur de la clé
def longueur_clef(cipher):
    """
    Documentation à écrire
    """
    
    longueurCle = 0
    
    for i in range (2,20):
        longueurCle = i
        tabColonne = [""]*longueurCle
        compteur = 0
        
        #Decoupe le texte en x colonne, x etant la longueurCLe
        for c in cipher:
            tabColonne[compteur] += c
            
            
            if compteur == longueurCle - 1 :
                compteur = 0
            else:
                compteur += 1
        
        #Calcul moyenne d'indice de coincidence de chaque colonne
        compteur = 0
        listIndC = [0.0] * longueurCle
        for j in tabColonne:
            #print(indice_coincidence(freq(j)))
            listIndC[compteur] = indice_coincidence(freq(j))
                
        if sum(listIndC) > 0.06:
            longueurCle = i
            break        
    
    return longueurCle
    
# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en utilisant la lettre la plus fréquente
# de chaque colonne
def clef_par_decalages(cipher, key_length):
    """
    Documentation à écrire
    """
    decalages=[0]*key_length
    tabColonne = [""]*key_length
    compteur = 0
    
    #Separation du texte en colonne
    for c in cipher:
            tabColonne[compteur] += c       
            
            if compteur == key_length - 1 :
                compteur = 0
            else:
                compteur += 1
    #Cherche freqMax
    i = 0
    for txt in tabColonne :
        if alphabet.index('E') < lettre_freq_max(txt):
            decalages[i] = lettre_freq_max(txt) - alphabet.index('E')
        elif alphabet.index('E') == lettre_freq_max(txt):
            decalages[i] = 0
        else:
            decalages[i] = lettre_freq_max(txt) + 26 - alphabet.index('E')
        
        i += 1
    
    
    return decalages

# Cryptanalyse V1 avec décalages par frequence max
def cryptanalyse_v1(cipher):
    """
    On obtient notre clef que grace aux decalages par rapport à la lettre E
    Mais tous les textes ne sont pas representatif de ce decalage en rapport à la lettre E (par rapport au texte GERMINAL)
    Du coup pour des textes representatif (peu présent) on arrive à déchiffrer le texte cipher
    """
    key_length = longueur_clef(cipher)
    decalages = clef_par_decalages(cipher, key_length)  
    txt_clair = dechiffre_vigenere(cipher, decalages)
    
    return txt_clair


################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V2.

# Indice de coincidence mutuelle avec décalage
def indice_coincidence_mutuelle(h1,h2,d):
    """
    Documentation à écrire
    """
    ICM = 0
    newh2 = [0.0] * len(alphabet)
    compteur = 0
    for i in h2 :
        newh2[(compteur - d) % 26] = h2[compteur]
        compteur += 1
    
    for i in range(0,26) :
        ICM += (h1[i]*newh2[i]) / (sum(h1)*sum(h2))
        
    return ICM

# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en comparant l'indice de décalage mutuel par rapport
# à la première colonne
def tableau_decalages_ICM(cipher, key_length):
    """
    Documentation à écrire
    """
    decalages=[0]*key_length
    tabColonne = [""]*key_length
    
    compteur = 0
    
    #Separation du texte en colonne
    for c in cipher:
            tabColonne[compteur] += c       
            
            if compteur == key_length - 1 :
                compteur = 0
            else:
                compteur += 1
    
    h1 = freq(tabColonne[0])
    listICM = [0.0] * len(alphabet)
    
    
    for i in range(1,key_length):
        #d indice de decalage     
        for d in range(1,26):     
            listICM[d] = indice_coincidence_mutuelle(h1, freq(tabColonne[i]), d)
        
        #on affecte d qui maximise ICM    
        decalages[i] = listICM.index(max(listICM))
        
    return decalages

# Cryptanalyse V2 avec décalages par ICM
def cryptanalyse_v2(cipher):
    """
    ON CHERCHE PAR RAPPORT À LA LETTRE LA PLUS PRESENTE DANS UN TEXTE FRANCAIS
    la frequence des lettres dans un texte peuvent varier
    """
    key_length = longueur_clef(cipher)
    decalages = tableau_decalages_ICM(cipher, key_length)   
    txt_chiffre = dechiffre_vigenere(cipher, decalages)
    print(freq(txt_chiffre))
    lettreFreqMax = lettre_freq_max(txt_chiffre)
    print(lettreFreqMax)
    indiceD = (lettreFreqMax - alphabet.index('E')) % 26
    
    return dechiffre_cesar(txt_chiffre, indiceD)


################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V3.

# Prend deux listes de même taille et
# calcule la correlation lineaire de Pearson
def correlation(L1,L2):
    """
    Documentation à écrire
    """
    return 0.0

# Renvoie la meilleur clé possible par correlation
# étant donné une longueur de clé fixée
def clef_correlations(cipher, key_length):
    """
    Documentation à écrire
    """
    key=[0]*key_length
    score = 0.0
    return (score, key)

# Cryptanalyse V3 avec correlations
def cryptanalyse_v3(cipher):
    """
    Documentation à écrire
    """
    return "TODO"


################################################################
# NE PAS MODIFIER LES FONCTIONS SUIVANTES
# ELLES SONT UTILES POUR LES TEST D'EVALUATION
################################################################


# Lit un fichier et renvoie la chaine de caracteres
def read(fichier):
    f=open(fichier,"r")
    txt=(f.readlines())[0].rstrip('\n')
    f.close()
    return txt

# Execute la fonction cryptanalyse_vN où N est la version
def cryptanalyse(fichier, version):
    cipher = read(fichier)
    if version == 1:
        return cryptanalyse_v1(cipher)
    elif version == 2:
        return cryptanalyse_v2(cipher)
    elif version == 3:
        return cryptanalyse_v3(cipher)

def usage():
    print()
    print ("Usage: python3 cryptanalyse_vigenere.py -v <1,2,3> -f <FichierACryptanalyser>", file=sys.stderr)
    sys.exit(1)

def main(argv):
    size = -1
    version = 0
    fichier = ''
    try:
        opts, args = getopt.getopt(argv,"hv:f:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-v"):
            version = int(arg)
        elif opt in ("-f"):
            fichier = arg
    if fichier=='':
        usage()
    if not(version==1 or version==2 or version==3):
        usage()

    print("Cryptanalyse version "+str(version)+" du fichier "+fichier+" :")
    print(cryptanalyse(fichier, version))
    
if __name__ == "__main__":
   main(sys.argv[1:])
